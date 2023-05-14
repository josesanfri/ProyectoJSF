// Check if api fetch is valid
export async function unWrap(response) {
  try {
    const json = await response.json();
    const { ok, status, statusText } = response;

    return {
      json,
      ok,
      status,
      statusText,
    };
  } catch (error) {
    getErrorResponse(error);
  }
}

// Check if api fetch is not valid
export function getErrorResponse(error) {
  return {
    ok: false,
    status: 500,
    statusText: error.message,
    json: {},
  };
}
