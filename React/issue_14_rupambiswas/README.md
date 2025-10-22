# Digital Clock with Alarm in React

This is a simple React component that displays a digital clock and allows setting an alarm. It updates in real-time and triggers a beep sound and alert when the alarm time is reached.

## Features
- Displays current time in HH:MM:SS (24-hour format).
- Set alarm via input (validated format).
- Plays a beep sound (using Web Audio API) and shows an alert on trigger.
- Reset functionality.

## How to Run
1. Ensure you have a React app set up (e.g., via Vite: `npm create vite@latest my-app -- --template react`).
2. Create a `src/components` folder if it doesn't exist.
3. Add `DigitalClockAlarm.jsx` to `src/components/`.
4. Update `src/App.jsx` to import and render `<DigitalClockAlarm />`.
5. Install dependencies if needed: `npm install`.
6. Start the dev server: `npm run dev`.
7. Open `http://localhost:5173` (or your port) in a browser.

## Notes
- Time is local to the client's machine.
- Sound requires browser support for Web Audio API (most modern browsers do).
- Test alarm by setting a time a few seconds ahead.

Built with React 18+. No external libraries required.