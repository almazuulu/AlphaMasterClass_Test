import pandas as pd

def load_referral_tree(csv_path):
    client_data = pd.read_csv(csv_path)
    referral_tree = {}
    for index, row in client_data.iterrows():
        email = row['email']
        ref_email = row['referral_email']
        if pd.isna(ref_email):  # If the referral_email is NaN, it's a root node
            referral_tree[email] = []
        else:
            if ref_email in referral_tree:
                referral_tree[ref_email].append(email)
            else:
                referral_tree[ref_email] = [email]
    return referral_tree

def get_referrals(email, referral_tree, level=0):
    """Recursively finds all referrals for a given email."""
    output = []
    if email in referral_tree:
        for referral in referral_tree[email]:
            output.append(('>' * level + ' ' + referral, level + 1))
            output.extend(get_referrals(referral, referral_tree, level + 1))
    return output
