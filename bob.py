def response(hey_bob):
    stripped = hey_bob.strip()
    if stripped.isupper() and stripped.endswith("?"):
        return "Calm down, I know what I'm doing!"
    if stripped.endswith("?"):
        return "Sure."
    if stripped.isupper():
        return "Whoa, chill out!"
    if not stripped:
        return "Fine. Be that way!"
    else:
        return "Whatever."

print(response("FCECDFCAAB"))