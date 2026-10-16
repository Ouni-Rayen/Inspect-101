# SEC Club — Inspect the Source (Beginner Web CTF)

## Theme
Club colors: deep navy background, cyan glow accents, soft lavender text.

## Challenge Concept
Players must inspect the page source to discover a linked JavaScript file that contains hardcoded login credentials. After logging in they receive the flag.

## Player Flow
1. Open the login page
2. View page source (Ctrl+U / right-click → View Source)
3. Notice the script tag pointing to `/static/auth.js`
4. Open that JS file → find the hardcoded username & password
5. Log in with those credentials
6. Flag is displayed on the success page

## Credentials (for organizers)
- Username: `club_member`
- Password: `CyanGlow2024!`

## Flag
`Securinets{4lways_Inspect_sOurce_c0de}`

## Quick Start with Docker

```bash
docker build -t inspect-source-ctf .
docker run -d -p 5000:5000 --name source-ctf inspect-source-ctf
```

Then open http://localhost:5000

Stop:
```bash
docker stop source-ctf && docker rm source-ctf
```

## Local run
```bash
pip install -r requirements.txt
python app.py
```

## Notes
- Pure source-code inspection challenge
- No real authentication complexity
- All styling follows the club color palette (no logo used)
