const API_URL = "http://127.0.0.1:5000/";

interface ApiResponse { 
  confidence: number; 
  answer: string; 
}

export const sendMessage = async (message: string): Promise<ApiResponse> => {
  try {
    const response = await fetch(`${API_URL}bot/question?question=${encodeURIComponent(message)}`);
    
    if (!response.ok) {
      throw new Error('Erro no servidor.');
    }

    const data: ApiResponse = await response.json();
    return data;

  } catch (error) {
    console.error('There was a problem with the fetch operation:', error);
    return { confidence: 0, answer: "Erro no servidor. Refaça sua pergunta, por favor" };
  }
}
