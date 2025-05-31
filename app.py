{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyMiIXaYHm3Rt1ot3Ul0cGtn",
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/AliRaza936/simple-calculator/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 1,
      "metadata": {
        "id": "xgTYLKYsFNCV",
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "outputId": "3505b5a4-573a-49e6-e58c-2aa27baaec77"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Simple Calculator\n",
            "Select operation:\n",
            "1. Add\n",
            "2. Subtract\n",
            "3. Multiply\n",
            "4. Divide\n",
            "Enter choice (1/2/3/4): 2\n",
            "Enter first number: 2\n",
            "Enter second number: 2\n",
            "2.0 - 2.0 = 0.0\n"
          ]
        }
      ],
      "source": [
        "# Simple Calculator in Google Colab\n",
        "\n",
        "def calculator():\n",
        "    print(\"Simple Calculator\")\n",
        "    print(\"Select operation:\")\n",
        "    print(\"1. Add\")\n",
        "    print(\"2. Subtract\")\n",
        "    print(\"3. Multiply\")\n",
        "    print(\"4. Divide\")\n",
        "\n",
        "    choice = input(\"Enter choice (1/2/3/4): \")\n",
        "\n",
        "    if choice not in ['1', '2', '3', '4']:\n",
        "        print(\"Invalid input\")\n",
        "        return\n",
        "\n",
        "    try:\n",
        "        num1 = float(input(\"Enter first number: \"))\n",
        "        num2 = float(input(\"Enter second number: \"))\n",
        "    except ValueError:\n",
        "        print(\"Invalid number input.\")\n",
        "        return\n",
        "\n",
        "    if choice == '1':\n",
        "        print(f\"{num1} + {num2} = {num1 + num2}\")\n",
        "    elif choice == '2':\n",
        "        print(f\"{num1} - {num2} = {num1 - num2}\")\n",
        "    elif choice == '3':\n",
        "        print(f\"{num1} * {num2} = {num1 * num2}\")\n",
        "    elif choice == '4':\n",
        "        if num2 == 0:\n",
        "            print(\"Error: Division by zero.\")\n",
        "        else:\n",
        "            print(f\"{num1} / {num2} = {num1 / num2}\")\n",
        "\n",
        "# Run the calculator\n",
        "calculator()\n"
      ]
    }
  ]
}