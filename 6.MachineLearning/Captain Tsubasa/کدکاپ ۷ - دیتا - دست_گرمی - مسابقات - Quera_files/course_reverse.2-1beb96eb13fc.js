function course_urls(viewName, ownerType, userToken, assignmentId, ...args) {
  if (userToken) {
    let res = userToken.split(":");
    let newViewName = res[0] + ":private:" + res.slice(1).join(":");
    return quera_urls[newViewName](ownerType, userToken, ...args);
  } else {
    return quera_urls[viewName](ownerType, assignmentId, ...args);
  }
}
