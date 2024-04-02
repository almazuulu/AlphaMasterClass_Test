document.addEventListener('DOMContentLoaded', (event) => {
    document.getElementById('referralForm').addEventListener('submit', function(event) {
        event.preventDefault();
        var emailInput = document.getElementById('client_email');
        var email = emailInput.value;
        fetch('/get_referrals', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ email: email }),
        })
        .then(response => response.json())
        .then(data => {
            document.getElementById('result').innerText = data.referrals.join('\n');
        })
        .catch((error) => {
            console.error('Error:', error);
            document.getElementById('result').innerText = 'Error fetching the referral hierarchy.';
        });
    });
});
