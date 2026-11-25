"""Agent framework tests. Uses a temporary data directory; touches no repo data."""
import importlib.util, json, os, tempfile, unittest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TMP = tempfile.mkdtemp(prefix="agents-test-")
os.environ["AGENT_DATA_DIR"] = TMP
spec = importlib.util.spec_from_file_location("orch", os.path.join(ROOT, "agents", "orchestrator.py"))
orch = importlib.util.module_from_spec(spec); spec.loader.exec_module(orch)

REQUIRED = ["id", "name", "team", "kind", "implemented", "input_contract", "output_contract", "allowed_tools", "permissions", "trigger",
            "retry_limit", "evidence", "validation", "human_approval", "failure_recovery", "status"]


class Registry(unittest.TestCase):
    def test_spec_complete(self):
        ids = [a["id"] for a in orch.REG]
        self.assertEqual(len(ids), 40); self.assertEqual(len(set(ids)), 40)
        for a in orch.REG:
            for k in REQUIRED: self.assertIn(k, a, a["id"])

    def test_implemented_means_callable(self):
        for a in orch.REG:
            self.assertEqual(a["implemented"], a["id"] in orch.IMPL, a["id"])

    def test_credential_agents_not_marked_implemented(self):
        for a in orch.REG:
            if a["status"] == "blocked_needs_credentials": self.assertFalse(a["implemented"])


class Runtime(unittest.TestCase):
    def setUp(self):
        stop = os.path.join(TMP, "STOP")
        if os.path.exists(stop): os.unlink(stop)

    def test_implemented_agent_runs(self):
        r = orch.run_agent("website_inventory")
        self.assertEqual(r["status"], "OK"); self.assertGreater(r["summary"]["routes"], 100)

    def test_unconfigured_agent_blocked_without_output(self):
        r = orch.run_agent("ai_visibility")
        self.assertEqual(r["status"], "BLOCKED"); self.assertIsNone(r["output"])

    def test_needs_built_dir_is_blocked_not_faked(self):
        self.assertEqual(orch.run_agent("technical_seo")["status"], "BLOCKED")

    def test_emergency_stop(self):
        open(os.path.join(TMP, "STOP"), "w").write("x")
        self.assertEqual(orch.run_agent("website_inventory")["status"], "REFUSED_EMERGENCY_STOP")

    def test_lock_prevents_concurrent_writer(self):
        with orch.lock("out-website_inventory"):
            self.assertEqual(orch.run_agent("website_inventory")["status"], "REFUSED_RESOURCE_LOCKED")

    def test_publishing_never_deploys(self):
        r = orch.run_agent("publishing")
        self.assertEqual(r["status"], "OK"); self.assertFalse(r["summary"]["deploys"])

    def test_ledger_written(self):
        orch.run_agent("keyword_intelligence")
        rows = [json.loads(l) for l in open(os.path.join(TMP, "ledger.jsonl"))]
        self.assertTrue(rows and all("task_id" in r and "status" in r for r in rows))


if __name__ == "__main__":
    unittest.main()
