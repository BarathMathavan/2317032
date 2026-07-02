import Log from './logger';

async function fetchWithLogging(url, options = {}, packageName = 'api') {
  const method = (options.method || 'GET').toUpperCase();
  const start = Date.now();
  try {
    Log('frontend', 'debug', packageName, `request:start ${method} ${url}`, { url, method });
    const res = await fetch(url, options);
    const duration = Date.now() - start;
    if (!res.ok) {
      Log('frontend', 'error', packageName, `request:fail ${method} ${url}`, { status: res.status, duration });
    } else {
      Log('frontend', 'info', packageName, `request:success ${method} ${url}`, { status: res.status, duration });
    }
    return res;
  } catch (err) {
    const duration = Date.now() - start;
    Log('frontend', 'error', packageName, `request:error ${method} ${url} - ${err && err.message}`, { duration });
    throw err;
  }
}

export { fetchWithLogging };

export default {
  get: (url, opts) => fetchWithLogging(url, { ...opts, method: 'GET' }, 'api'),
  post: (url, body, opts = {}) => fetchWithLogging(url, { ...opts, method: 'POST', body: JSON.stringify(body), headers: { 'Content-Type': 'application/json', ...(opts.headers||{}) } }, 'api'),
};
