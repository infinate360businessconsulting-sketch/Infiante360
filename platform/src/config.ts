import { z } from "zod";
const schema = z.object({
  PORT: z.coerce.number().default(8080),
  PUBLIC_ORIGIN: z.string().url(),
  DATABASE_URL: z.string().optional(),
  ADMIN_API_KEY: z.string().min(24),
  SESSION_SECRET: z.string().min(24),
  WEBINAR_GG_API_TOKEN: z.string().optional(),
  WEBINAR_GG_API_BASE: z.string().url().default("https://webinar-api.webinar.gg/api/v1"),
  ANTHROPIC_API_KEY: z.string().optional(),
  ANTHROPIC_MODEL: z.string().optional(),
});
export type Config = z.infer<typeof schema>;
export const loadConfig = (env: NodeJS.ProcessEnv = process.env): Config => schema.parse(env);
