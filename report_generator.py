from instagram_client import get_followers_count, get_inactive_users

def generate_report():
    total_followers = get_followers_count()
    inactive = get_inactive_users()

    report = f"\ud83d\udcca Instagram Daily Report:\n"
    report += f"Total Followers: {total_followers}\n"
    report += f"Inactive Followers: {len(inactive)}\n"
    if inactive:
        report += f"Examples: {', '.join(inactive[:5])}"
    return report