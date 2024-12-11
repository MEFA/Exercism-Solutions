def response(hey_bob):
    stripped = hey_bob.strip()
    if stripped.endswith == "?":
        return "Sure."
    if stripped.endswith == "!":
        return "Whoa, chill out!"
    if stripped.isupper() and stripped.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if not stripped:
        return "Fine. Be that way!"
    else:
        return "Whatever."

print(response("WHAT'S GOING ON?"))