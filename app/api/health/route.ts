export async function GET() {
  return new Response(JSON.stringify({
    status: 'healthy',
    timestamp: new Date().toISOString(),
    version: process.env.RAILWAY_GIT_COMMIT_SHA?.slice(0, 7) || 'local'
  }), {
    status: 200,
    headers: { 'Content-Type': 'application/json' }
  });
}