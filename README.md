# Piston (My Physics Simulation!)

Hey! 👋 Welcome to **Piston**. This is a cool little Python project I cooked up to simulate the physics of a motor's rotational motion being converted into linear motion. Think of it as a virtual engine, but way less greasy!

It visualizes this conversion using an animated graph, so you can actually *see* the piston moving. It's a fun way to bring physics to life with code!

## 📂 What's in the Repo?

Just two main files keep this simulation chugging along:

*   **`piston.py`**: This is the core Python script that runs the entire physics simulation and generates the animated graph. It's where all the magic happens!
*   **`README.md`**: (You're reading it!)

## 🛠️ Tech Stack

*   **Python**: My go-to language for scripting and simulations.

## ⚙️ How It Works (and How to Run It!)

This simulation works independently. To get it going, you'll need to provide a few initial values:

*   **Radius of the motor arm**
*   **Length of the connected arm**
*   **Interval (in angles) after which data is recorded**

Once you run `piston.py`, it will take these inputs and show you the animated motion!

```bash
# First, navigate to the project folder
cd Piston

# Then, run the simulation
python piston.py
