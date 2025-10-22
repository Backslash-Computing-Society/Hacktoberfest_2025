import React, { useState, useEffect, useRef } from "react";

// DigitalClockAlarm Component
// Displays a live digital clock (HH:MM:SS) and lets users set an alarm
export default function DigitalClockAlarm() {
  const [time, setTime] = useState(getCurrentTime());
  const [alarmTime, setAlarmTime] = useState(""); // HH:MM[:SS]
  const [alarmEnabled, setAlarmEnabled] = useState(false);
  const [alarmTriggered, setAlarmTriggered] = useState(false);

  const alarmRef = useRef(""); // normalized alarm time for comparison

  // Update time every 250ms
  useEffect(() => {
    const interval = setInterval(() => {
      const now = getCurrentTime();
      setTime(now);

      if (alarmEnabled && alarmRef.current && !alarmTriggered) {
        if (timesMatch(now, alarmRef.current)) {
          triggerAlarm();
        }
      }
    }, 250);

    return () => clearInterval(interval);
  }, [alarmEnabled, alarmTriggered]);

  // Format current time as HH:MM:SS
  function getCurrentTime() {
    const now = new Date();
    return [
      pad(now.getHours()),
      pad(now.getMinutes()),
      pad(now.getSeconds()),
    ].join(":");
  }

  // Pad single digit numbers with 0
  function pad(num) {
    return num.toString().padStart(2, "0");
  }

  // Normalize alarm input to HH:MM:SS
  function normalizeInputToHHMMSS(input) {
    if (!input) return "";
    const parts = input.split(":");
    if (parts.length === 2) return `${pad(parts[0])}:${pad(parts[1])}:00`;
    if (parts.length === 3) return `${pad(parts[0])}:${pad(parts[1])}:${pad(parts[2])}`;
    return "";
  }

  // Compare clock time with alarm time
  function timesMatch(current, alarm) {
    return current === alarm;
  }

  // Trigger alarm: show message & beep
  function triggerAlarm() {
    setAlarmTriggered(true);
    playBeep();
    alert(`⏰ Alarm! It's ${alarmRef.current}`);
    // Reset after triggering
    setTimeout(() => {
      setAlarmTriggered(false);
      setAlarmEnabled(false);
      setAlarmTime("");
      alarmRef.current = "";
    }, 1000);
  }

  // Simple beep using Web Audio API
  function playBeep() {
    const audioCtx = new (window.AudioContext || window.webkitAudioContext)();
    const oscillator = audioCtx.createOscillator();
    oscillator.type = "sine";
    oscillator.frequency.setValueAtTime(1000, audioCtx.currentTime); // 1000Hz beep
    oscillator.connect(audioCtx.destination);
    oscillator.start();
    oscillator.stop(audioCtx.currentTime + 0.5); // beep for 0.5s
  }

  // Handle alarm set
  function handleSetAlarm(e) {
    e.preventDefault();
    const normalized = normalizeInputToHHMMSS(alarmTime);
    if (!normalized) {
      alert("Please pick a valid alarm time.");
      return;
    }
    alarmRef.current = normalized;
    setAlarmEnabled(true);
    setAlarmTriggered(false);
    alert(`✅ Alarm set for ${normalized}`);
  }

  return (
    <div style={{ fontFamily: "sans-serif", textAlign: "center", marginTop: "20px" }}>
      <h2>Current Time</h2>
      <div style={{ fontSize: "3rem", margin: "10px 0" }}>{time}</div>

      <form onSubmit={handleSetAlarm} style={{ marginTop: "20px" }}>
        <label>
          Set Alarm:
          <input
            type="time"
            step="1"
            value={alarmTime}
            onChange={(e) => setAlarmTime(e.target.value)}
            style={{ marginLeft: "10px" }}
          />
        </label>
        <button type="submit" style={{ marginLeft: "10px", padding: "5px 10px" }}>
          Set
        </button>
      </form>

      {alarmEnabled && <p>⏰ Alarm is set for {alarmRef.current}</p>}
    </div>
  );
}
