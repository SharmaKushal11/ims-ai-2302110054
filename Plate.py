{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyP9rrQxwLB5zitAw4D2GQ/P",
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
        "<a href=\"https://colab.research.google.com/github/SharmaKushal11/ims-ai-2302110054/blob/main/Plate.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "3UiU04T9hLuE"
      },
      "outputs": [],
      "source": [
        "\n",
        "!pip install -q cadquery\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from cadquery import func as cf\n",
        "\n",
        "plate = cf.box(80, 50, 10)       # length, width, height (mm)\n",
        "hole = cf.cylinder(d=20, h=10)   # diameter, height\n",
        "part = plate - hole              # subtract = drill!\n",
        "\n",
        "print(part.isValid(), round(part.Volume(), 1))\n",
        "part.exportStl(\"plate.stl\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "CaFZ1wDphq3Q",
        "outputId": "94b9627e-6e16-4fbb-f042-95ecc81fbbb5"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True 36858.4\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 2
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from cadquery import func as cf\n",
        "\n",
        "plate = cf.box(80, 50, 10)             # length, width, height (mm)\n",
        "hole = cf.cylinder(d=20, h=10).moved(x=20)  # diameter, height\n",
        "part = plate - hole                    # subtract = drill!\n",
        "\n",
        "print(part.isValid(), round(part.Volume(), 1))\n",
        "part.exportStl(\"plate.stl\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MO5PrXNfhyMM",
        "outputId": "44aff37c-dafe-47f4-b714-d300f5e3737e"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "True 36858.4\n"
          ]
        },
        {
          "output_type": "execute_result",
          "data": {
            "text/plain": [
              "True"
            ]
          },
          "metadata": {},
          "execution_count": 3
        }
      ]
    }
  ]
}