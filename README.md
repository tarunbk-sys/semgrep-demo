# semgrep-demo

A tiny Flask app with **intentionally insecure code**, used to test
Semgrep scanning via GitHub Actions.

Expected findings include SQL injection, command injection, use of
`eval`, weak hashing (MD5), Flask debug mode, and an outdated Flask
dependency (if Supply Chain scanning is enabled).

Do not deploy this code.
