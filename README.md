

# 🔐 OTP CTF Lab

Welcome to the **OTP CTF Lab**, a deliberately vulnerable OTP (One-Time Password) authentication system built with Python & Flask.

This lab is designed to show how insecure implementations of OTP can be bypassed.

---

## 🚀 Storyline

You’ve just signed up to a brand-new social media clone.
Before you can log in, the app requires you to verify your identity with a **4-digit OTP**.

Sounds easy, right? But the developers made a few *mistakes*… 👀

Your mission is to:

1. Sign up with any details.
2. Capture the OTP verification request.
3. Find a way to bypass the OTP protection.

---

## ⚙️ Setup Instructions

1. Clone this repository:

   ```bash
   git clone https://github.com/Cybernuel/otp_bypass_simulation.git
   cd otp_bypass_simulation
   ```

3. Run the Flask server:

   ```bash
   python app.py
   ```

4. Open your browser and visit:

   ```
   http://127.0.0.1:5000
   ```

---

## 🎯 Challenge

* Sign up using the form (any fake details work).
* You’ll be redirected to the OTP verification page.
* But here’s the twist: the OTP system has **a few vulnerabilities**.

🔍 **Your task:**
Figure out how to bypass the OTP check and reach the **success page**.

💡 *Hint*: Tools like **Burp Suite** will make your life a lot easier.

---

## 📚 What You’ll Learn

* How small logic flaws in OTP validation can break the entire authentication process.
* Why security through “just adding OTP” is not enough.
* The importance of testing authentication flows like an attacker.

---

## ⚠️ Disclaimer

This lab is for **educational purposes only**.
Do not use these techniques on real systems without permission.

