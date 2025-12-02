const BASE_URL = 'http://localhost:8000'; // Match your FastAPI server port

export const fetchInsight = async (query) => {
  const response = await fetch(`${BASE_URL}/api/rag_insights`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({ query }),
  });

  if (!response.ok) {
    throw new Error('Failed to get insight from AI Co-Pilot.');
  }

  const data = await response.json();
  return data.insight;
};