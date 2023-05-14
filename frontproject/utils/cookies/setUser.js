import Cookie from "js-cookie";

export function setUserCookies(data) {
  let { token, user_id, email, user_type } = data;

  Cookie.set("leg__token", token, {
    expires: 1 / 24,
    path: "/",
    sameSite: "Lax",
  });
  Cookie.set("leg__id", user_id, {
    expires: 1 / 24,
    path: "/",
    sameSite: "Lax",
  });
  Cookie.set("leg__email", email, {
    expires: 1 / 24,
    path: "/",
    sameSite: "Lax",
  });
  Cookie.set("leg__user_type", user_type, {
    expires: 1 / 24,
    path: "/",
    sameSite: "Lax",
  });
}
