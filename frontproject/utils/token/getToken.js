import Cookies from "js-cookie";

export default function (store) {
  let token;
  try {
    token = Cookies.get("leg__token");
  } catch {
    if (process.env.client) {
      token = store.getters.auth.getToken;
    }

    console.info("INCOGNITO WINDOW ENABLED");
  }

  return token;
}
