// Frontend logging middleware
const STACK_ALLOWED = new Set(["frontend"]);
const LEVEL_ALLOWED = new Set(["debug", "info", "warn", "error", "fatal"]);
const PACKAGE_ALLOWED = new Set([
  "api",
  "component",
  "hook",
  "page",
  "state",
  // shared
  "auth",
  "config",
  "middleware",
  "utils",
  "style",
]);

const TEST_SERVER_URL = "http://4.224.186.213/evaluation-service/logs";

// token may be set at runtime with setAuthToken or via localStorage 'authToken'
let AUTH_TOKEN = typeof window !== 'undefined' ? window.localStorage.getItem('authToken') : null;

export function setAuthToken(token) {
  AUTH_TOKEN = token;
  try {
    if (typeof window !== 'undefined' && token) window.localStorage.setItem('authToken', token);
  } catch (e) {
    // ignore
  }
}

async function sendToServer(payload) {
  try {
    const headers = { "Content-Type": "application/json" };
    const token = AUTH_TOKEN || (typeof window !== 'undefined' && window.localStorage.getItem('authToken'));
    if (token) headers.Authorization = `Bearer ${token}`;

    await fetch(TEST_SERVER_URL, {
      method: "POST",
      headers,
      body: JSON.stringify(payload),
    });
  } catch (e) {
    // Don't throw from logger
    console.warn("Logger: failed to send log", e);
  }
}

async function Log(stack, level, packageName, message, meta = {}) {
  try {
    if (typeof stack !== "string" || typeof level !== "string" || typeof packageName !== "string") {
      console.warn("Log: stack, level and package must be strings (lowercase)");
      return;
    }

    const s = stack.toLowerCase();
    const l = level.toLowerCase();
    const p = packageName.toLowerCase();

    if (!STACK_ALLOWED.has(s)) {
      console.warn(`Log: invalid stack '${stack}'. Using 'frontend'`);
      // allow fallback
    }
    if (!LEVEL_ALLOWED.has(l)) {
      console.warn(`Log: invalid level '${level}'. Using 'info'`);
    }
    if (!PACKAGE_ALLOWED.has(p)) {
      console.warn(`Log: package '${packageName}' is uncommon; still sending.`);
    }

    const payload = {
      stack: s,
      level: l,
      package: p,
      message: typeof message === "string" ? message : JSON.stringify(message),
      timestamp: new Date().toISOString(),
      meta,
    };

    // Log locally for development visibility
    if (l === "error" || l === "fatal") console.error("Log:", payload);
    else if (l === "warn") console.warn("Log:", payload);
    else console.log("Log:", payload);

    // Send to test server (non-blocking)
    void sendToServer(payload);
  } catch (err) {
    console.error("Log: unexpected error", err);
  }
}

export default Log;
