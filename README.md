# 💻 MyProctorAI - An Online Exam Proctoring Solution

*Last updated on June 02, 2022*

## Table of Contents

[Introduction](#introduction)

[User Guide](#user-guide)

[Developer's Guide](#developers-guide)

# User Guide

## Introduction

In this era of online examination, there are numerous online examination platforms readily available in the market. But the functionality they lack is the proper proctoring system. The MyProctorAI is - ** a demo of proctoring equipped examination platform which is cheating proof to nearly all possibilities.** 

## Features

This project is equipped with - 
- Recording real time movement from user's device camera and detecting any suspecious activities that can lead to cheating.
- Recording the user's audio from your devices audio input and log the records.
- Recording the user's active screen to check on screen activities happening.

Furthermore, The features which are in development are - 
- Face Detection Module - To ensure only one candidate is present on the screen.
- Face Recognition Module - To ensure the allowed candidae is attempting the exam. 

And there are features which I have planned to include, 

# Developer's Guide

## ⚙ Installation Steps

1. Install Python, Add it to the System Environment Variables.
2. Open the project in VSCode.
3. Run `pip install virtualenv ` to install virtual environment.
4. Run `virtualenv env` to create a new virtual environment.
5. Run `Set-ExecutionPolicy unrestricted`, if it throws an error, run the same command in Admin PowerShell, and when prompted press `A`.
6. 🔸 Run `.\env\Scripts\activate.ps1` to enable virtualenv.
7. Run `pip install flask`.
8. Run `export FLASK_ENV=development` to change the environment to development.

