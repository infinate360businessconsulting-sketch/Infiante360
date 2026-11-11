CREATE TABLE IF NOT EXISTS activation_codes (
  code TEXT PRIMARY KEY,
  plan TEXT NOT NULL,
  batch TEXT NOT NULL,
  expires_at TIMESTAMPTZ,
  redeemed_by TEXT,
  redeemed_at TIMESTAMPTZ,
  created_at TIMESTAMPTZ DEFAULT NOW()
);
CREATE TABLE IF NOT EXISTS entitlements (
  email TEXT NOT NULL,
  plan TEXT NOT NULL,
  batch TEXT NOT NULL,
  expires_at TIMESTAMPTZ,
  PRIMARY KEY (email, plan, batch)
);
CREATE TABLE IF NOT EXISTS live_sessions (
  id TEXT PRIMARY KEY,
  title TEXT NOT NULL,
  plan TEXT NOT NULL,
  batch TEXT NOT NULL,
  webinar_id TEXT NOT NULL UNIQUE,
  scheduled_at TIMESTAMPTZ NOT NULL,
  duration_minutes INT NOT NULL,
  status TEXT NOT NULL DEFAULT 'scheduled'
);
CREATE INDEX IF NOT EXISTS idx_sessions_plan_batch ON live_sessions(plan, batch);
