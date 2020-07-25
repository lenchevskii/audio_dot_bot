## audio.BOT
Bot which save locally and convert audio messages into .wav (16 kHz), save photos' contain faces.

- [x] Telegram bot
- [ ] Tests

Create environment variables for running application (TOKEN) and tests (TELEGRAM_APP_ID, TELEGRAM_APP_HASH, TELETHON_SESSION):

```bash
export TOKEN=...
```

Saving occurs on server: 
- **../source/static/photo/user_id** for photos
- **../source/static/voice/user_id** for audio messages
