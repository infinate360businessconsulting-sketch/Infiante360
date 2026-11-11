import pg from "pg";
import { loadConfig } from "./config.js";
import { makeApp } from "./app.js";
import { MemoryStore } from "./store.js";
import { PgStore } from "./pgstore.js";
import { WebinarGg } from "./webinar.js";
import { loadKnowledge } from "./assistant.js";

const cfg = loadConfig();
const store = cfg.DATABASE_URL ? new PgStore(new pg.Pool({ connectionString: cfg.DATABASE_URL })) : new MemoryStore();
if (!cfg.DATABASE_URL) console.warn("DATABASE_URL not set: using in-memory store (development only)");
const webinar = cfg.WEBINAR_GG_API_TOKEN ? new WebinarGg(cfg.WEBINAR_GG_API_BASE, cfg.WEBINAR_GG_API_TOKEN) : undefined;
const chunks = loadKnowledge(new URL("../knowledge", import.meta.url).pathname);
makeApp({ cfg, store, webinar, chunks }).listen(cfg.PORT, () => console.log(`API on :${cfg.PORT}`));
