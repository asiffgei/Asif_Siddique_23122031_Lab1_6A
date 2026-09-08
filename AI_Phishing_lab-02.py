"""
Simple URL Safety Checker (Starter Version)
--------------------------------------------
User enters a URL, the program runs 3 basic checks on it,
gives a Safety Score out of 10, and a short review.

This is a starting point — more validations can be added later.
"""

def check_url(url):
    score = 10          # start with a perfect score
    reasons = []         # keep track of why points were deducted

    # ---- Validation 1: Does it use HTTPS? ----
    if url.startswith("https://"):
        reasons.append("✅ Uses HTTPS (secure connection)")
    else:
        score -= 4
        reasons.append("❌ Does NOT use HTTPS (-4)")

    # ---- Validation 2: Suspicious keywords in the URL ----
    suspicious_words = ["login", "verify", "secure", "account", "update", "bank"]
    found_words = [word for word in suspicious_words if word in url.lower()]

    if found_words:
        score -= 3
        reasons.append(f"❌ Contains suspicious word(s): {found_words} (-3)")
    else:
        reasons.append("✅ No suspicious keywords found")

    # ---- Validation 3: Is an IP address used instead of a domain name? ----
    import re
    domain_part = url.replace("https://", "").replace("http://", "").split("/")[0]
    is_ip = bool(re.match(r"^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$", domain_part))

    if is_ip:
        score -= 3
        reasons.append("❌ Uses an IP address instead of a domain name (-3)")
    else:
        reasons.append("✅ Uses a normal domain name")

    # Score should not go below 0
    score = max(score, 0)

    return score, reasons


def review(score):
    if score >= 8:
        return "🟢 Safe to visit"
    elif score >= 5:
        return "🟡 Suspicious — be careful"
    else:
        return "🔴 Unsafe — do not enter personal info"


def main():
    print("=== Simple URL Safety Checker ===")
    url = input("Enter a URL to check: ").strip()

    score, reasons = check_url(url)
    verdict = review(score)

    print("\n--- Report ---")
    for r in reasons:
        print(r)

    print(f"\nSafety Score: {score}/10")
    print(f"Review: {verdict}")


if __name__ == "__main__":
    main()