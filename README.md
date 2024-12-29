
# Metatron's Cube Classifier: A Study of Stylized Neural Networks

## 1. Executive Summary
This project explores the intersection of **sacred geometry** and **machine learning** by testing the predictive power of **Metatron's Cube** as the structure for a neural network classifier. Metatron's Cube, a symbol of balance, harmony, and interconnectedness, inspires the architecture of a neural network designed to solve a classification problem with five inputs and one output. Beyond functionality, this project delves into the aesthetics of neural network visualization, transforming the structure into an artistic and thought-provoking representation.

The project includes:
- Mapping Metatron's Cube to a neural network.
- A mathematical exploration of the classification problem.
- Visualizing the network with artistic styling.
- Examining the importance of the center node as a central component in the structure.

---

## 2. Introduction to Metatron's Cube
**Metatron's Cube** is a **sacred geometric pattern** made up of 13 circles of equal size interconnected by straight lines. It symbolizes the **balance, harmony, and interconnectedness** of all things in the universe. This structure is revered in various philosophical and spiritual traditions and is often associated with concepts of unity and divine energy.

From a geometric perspective:
- **13 circles**: Represent nodes in the network.
- **Connecting lines**: Represent relationships or connections between elements.
- It is a **two-dimensional representation** of a **three-dimensional shape**, and within its structure, it contains the five Platonic solids, foundational building blocks of geometry.

This project leverages the **spatial harmony** and connectivity of Metatron’s Cube to create a neural network inspired by its structure.

---

## 3. Testing the Predictive Power of Metatron's Cube

This project proposes to use Metatron's Cube as a **stylized neural network** architecture for a classification problem. The goal is to assess whether the cube's inherent structure, mapped to a neural network, can effectively model relationships between inputs and an output.

### 3.1. Classification Problem
The classification problem involves **five input features** (`x₁, x₂, x₃, x₄, x₅`) and **one binary output** (`y`). Mathematically, the classification task can be represented as a multivariate regression:

\[
y = \sigma(w_1x_1 + w_2x_2 + w_3x_3 + w_4x_4 + w_5x_5 + b)
\]

Where:
- \( \sigma \) is the sigmoid activation function to map the output to a probability.
- \( w_1, w_2, \ldots, w_5 \) are weights learned by the network.
- \( b \) is the bias term.

The network structure:
- **5 outer nodes** correspond to the inputs.
- **6 inner nodes** represent hidden layer neurons connected to the inputs and the center.
- **1 center node** integrates information from the inner nodes.
- **1 output node** generates the classification result.

### 3.2. Importance of the Center Node
The **center node** plays a pivotal role in the network:
- It acts as the **integration point**, aggregating information from the six inner nodes.
- Symbolically, the center node reflects the balance and harmony of Metatron’s Cube.
- Mathematically, it serves as an intermediate representation, condensing learned patterns before the output node.

This hierarchical structure mirrors Metatron’s Cube, where the center represents unity and connection.

---

## 4. Stylized Neural Networks
Beyond functionality, the project emphasizes the **aesthetics** of neural network visualization. The neural network inspired by Metatron's Cube is visualized as a stylized structure with:
- **Concentric circles**: Representing nodes in the network.
- **Golden lines**: Depicting connections between nodes.
- **Geometric harmony**: Aligning nodes and connections in a visually appealing way.

These stylizations are achieved through Python libraries such as `matplotlib` and `networkx`. The visualization not only makes the network easier to understand but also transforms it into a piece of art.

The final visualization includes:
- **Outer nodes** in a hexagonal arrangement.
- **Inner nodes** in a smaller hexagon.
- **A central node**, emphasized as the focal point of the structure.

---

## 5. Summary
This project marries **sacred geometry** with **machine learning**, exploring the predictive power of Metatron's Cube as the structure for a neural network. By mapping its geometric balance to a classifier, we:
- Demonstrate the potential for unconventional network architectures inspired by art and philosophy.
- Emphasize the importance of **stylized neural networks**, blending aesthetics with functionality.
- Highlight the unique role of the center node as a symbolic and functional integrator in the network.

Metatron's Cube is more than just a spiritual symbol; it serves as a bridge between **art, science, and machine learning**, sparking curiosity about the interplay between form and function.
