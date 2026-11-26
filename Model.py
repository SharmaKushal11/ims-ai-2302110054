{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyPsvNMhH/npfFnfyI52jaR0",
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
        "<a href=\"https://colab.research.google.com/github/SharmaKushal11/ims-ai-2302110054/blob/main/Model.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install cadquery"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "MyuSud3Cnoml",
        "outputId": "206b6f59-07fe-4e5c-d136-e0a3dd7dbd2e"
      },
      "execution_count": 2,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Collecting cadquery\n",
            "  Downloading cadquery-2.8.0-py3-none-any.whl.metadata (14 kB)\n",
            "Collecting cadquery-ocp<8.0,>=7.9.3.1 (from cadquery)\n",
            "  Downloading cadquery_ocp-7.9.3.1.1-cp313-cp313-manylinux_2_31_x86_64.whl.metadata (831 bytes)\n",
            "Collecting ezdxf>=1.3.0 (from cadquery)\n",
            "  Downloading ezdxf-1.4.5-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (10 kB)\n",
            "Collecting multimethod<2.0,>=1.11 (from cadquery)\n",
            "  Downloading multimethod-1.12-py3-none-any.whl.metadata (9.6 kB)\n",
            "Collecting nlopt<3.0,>=2.9.0 (from cadquery)\n",
            "  Downloading nlopt-2.11.0-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl.metadata (2.1 kB)\n",
            "Collecting runtype (from cadquery)\n",
            "  Downloading runtype-0.5.3-py3-none-any.whl.metadata (6.4 kB)\n",
            "Collecting casadi (from cadquery)\n",
            "  Downloading casadi-3.8.2-cp311-abi3-manylinux_2_28_x86_64.whl.metadata (2.2 kB)\n",
            "Collecting trame (from cadquery)\n",
            "  Downloading trame-4.0.0-py3-none-any.whl.metadata (8.7 kB)\n",
            "Collecting trame-vtk (from cadquery)\n",
            "  Downloading trame_vtk-2.11.17-py3-none-any.whl.metadata (14 kB)\n",
            "Collecting trame-components (from cadquery)\n",
            "  Downloading trame_components-2.5.0-py3-none-any.whl.metadata (3.7 kB)\n",
            "Collecting trame-vuetify (from cadquery)\n",
            "  Downloading trame_vuetify-3.3.0-py3-none-any.whl.metadata (5.5 kB)\n",
            "Requirement already satisfied: pyparsing>=3.0.0 in /usr/local/lib/python3.13/dist-packages (from cadquery) (3.3.3)\n",
            "Requirement already satisfied: scipy in /usr/local/lib/python3.13/dist-packages (from cadquery) (1.16.3)\n",
            "Requirement already satisfied: numba in /usr/local/lib/python3.13/dist-packages (from cadquery) (0.64.0)\n",
            "Collecting cadquery-ocp-proxy==7.9.3.1.1 (from cadquery-ocp<8.0,>=7.9.3.1->cadquery)\n",
            "  Downloading cadquery_ocp_proxy-7.9.3.1.1-py3-none-any.whl.metadata (5.2 kB)\n",
            "Collecting vtk==9.6.2 (from cadquery-ocp<8.0,>=7.9.3.1->cadquery)\n",
            "  Downloading vtk-9.6.2-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl.metadata (5.6 kB)\n",
            "Requirement already satisfied: matplotlib>=2.0.0 in /usr/local/lib/python3.13/dist-packages (from vtk==9.6.2->cadquery-ocp<8.0,>=7.9.3.1->cadquery) (3.10.0)\n",
            "Requirement already satisfied: numpy<3,>=2 in /usr/local/lib/python3.13/dist-packages (from nlopt<3.0,>=2.9.0->cadquery) (2.4.6)\n",
            "Requirement already satisfied: typing_extensions>=4.6.0 in /usr/local/lib/python3.13/dist-packages (from ezdxf>=1.3.0->cadquery) (4.16.0)\n",
            "Requirement already satisfied: fonttools in /usr/local/lib/python3.13/dist-packages (from ezdxf>=1.3.0->cadquery) (4.68.0)\n",
            "Requirement already satisfied: contourpy>=1.0.1 in /usr/local/lib/python3.13/dist-packages (from matplotlib>=2.0.0->vtk==9.6.2->cadquery-ocp<8.0,>=7.9.3.1->cadquery) (1.4.0)\n",
            "Requirement already satisfied: cycler>=0.10 in /usr/local/lib/python3.13/dist-packages (from matplotlib>=2.0.0->vtk==9.6.2->cadquery-ocp<8.0,>=7.9.3.1->cadquery) (0.12.1)\n",
            "Requirement already satisfied: kiwisolver>=1.3.1 in /usr/local/lib/python3.13/dist-packages (from matplotlib>=2.0.0->vtk==9.6.2->cadquery-ocp<8.0,>=7.9.3.1->cadquery) (1.5.1)\n",
            "Requirement already satisfied: packaging>=20.0 in /usr/local/lib/python3.13/dist-packages (from matplotlib>=2.0.0->vtk==9.6.2->cadquery-ocp<8.0,>=7.9.3.1->cadquery) (26.3)\n",
            "Requirement already satisfied: pillow>=8 in /usr/local/lib/python3.13/dist-packages (from matplotlib>=2.0.0->vtk==9.6.2->cadquery-ocp<8.0,>=7.9.3.1->cadquery) (11.3.0)\n",
            "Requirement already satisfied: python-dateutil>=2.7 in /usr/local/lib/python3.13/dist-packages (from matplotlib>=2.0.0->vtk==9.6.2->cadquery-ocp<8.0,>=7.9.3.1->cadquery) (2.9.0.post0)\n",
            "Requirement already satisfied: six>=1.5 in /usr/local/lib/python3.13/dist-packages (from python-dateutil>=2.7->matplotlib>=2.0.0->vtk==9.6.2->cadquery-ocp<8.0,>=7.9.3.1->cadquery) (1.17.0)\n",
            "Requirement already satisfied: llvmlite<0.47,>=0.46.0dev0 in /usr/local/lib/python3.13/dist-packages (from numba->cadquery) (0.46.0)\n",
            "Requirement already satisfied: pyyaml in /usr/local/lib/python3.13/dist-packages (from trame->cadquery) (6.0.3)\n",
            "Collecting trame-client<5,>=4 (from trame->cadquery)\n",
            "  Downloading trame_client-4.1.4-py3-none-any.whl.metadata (6.6 kB)\n",
            "Collecting trame-common<2,>=1.2.7 (from trame->cadquery)\n",
            "  Downloading trame_common-1.3.0-py3-none-any.whl.metadata (4.2 kB)\n",
            "Collecting trame-server<5,>=4 (from trame->cadquery)\n",
            "  Downloading trame_server-4.1.3-py3-none-any.whl.metadata (9.3 kB)\n",
            "Collecting wslink>=2.5.7 (from trame->cadquery)\n",
            "  Downloading wslink-2.6.0-py3-none-any.whl.metadata (3.3 kB)\n",
            "Requirement already satisfied: more-itertools in /usr/local/lib/python3.13/dist-packages (from trame-server<5,>=4->trame->cadquery) (10.8.0)\n",
            "Requirement already satisfied: aiohttp<4 in /usr/local/lib/python3.13/dist-packages (from wslink>=2.5.7->trame->cadquery) (3.14.5)\n",
            "Requirement already satisfied: msgpack<2,>=1 in /usr/local/lib/python3.13/dist-packages (from wslink>=2.5.7->trame->cadquery) (1.2.4)\n",
            "Requirement already satisfied: aiohappyeyeballs>=2.5.0 in /usr/local/lib/python3.13/dist-packages (from aiohttp<4->wslink>=2.5.7->trame->cadquery) (2.7.1)\n",
            "Requirement already satisfied: aiosignal>=1.4.0 in /usr/local/lib/python3.13/dist-packages (from aiohttp<4->wslink>=2.5.7->trame->cadquery) (1.4.0)\n",
            "Requirement already satisfied: attrs>=17.3.0 in /usr/local/lib/python3.13/dist-packages (from aiohttp<4->wslink>=2.5.7->trame->cadquery) (26.1.0)\n",
            "Requirement already satisfied: frozenlist>=1.1.1 in /usr/local/lib/python3.13/dist-packages (from aiohttp<4->wslink>=2.5.7->trame->cadquery) (1.8.0)\n",
            "Requirement already satisfied: multidict<8.0,>=4.5 in /usr/local/lib/python3.13/dist-packages (from aiohttp<4->wslink>=2.5.7->trame->cadquery) (7.2.1)\n",
            "Requirement already satisfied: propcache>=0.2.0 in /usr/local/lib/python3.13/dist-packages (from aiohttp<4->wslink>=2.5.7->trame->cadquery) (0.5.4)\n",
            "Requirement already satisfied: yarl<2.0,>=1.25.1 in /usr/local/lib/python3.13/dist-packages (from aiohttp<4->wslink>=2.5.7->trame->cadquery) (1.25.1)\n",
            "Requirement already satisfied: idna>=2.0 in /usr/local/lib/python3.13/dist-packages (from yarl<2.0,>=1.25.1->aiohttp<4->wslink>=2.5.7->trame->cadquery) (3.20)\n",
            "Downloading cadquery-2.8.0-py3-none-any.whl (201 kB)\n",
            "Downloading cadquery_ocp-7.9.3.1.1-cp313-cp313-manylinux_2_31_x86_64.whl (67.8 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m67.8/67.8 MB\u001b[0m \u001b[31m47.6 MB/s\u001b[0m  \u001b[33m0:00:01\u001b[0m\n",
            "\u001b[?25hDownloading cadquery_ocp_proxy-7.9.3.1.1-py3-none-any.whl (3.3 kB)\n",
            "Downloading vtk-9.6.2-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (146.0 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m146.0/146.0 MB\u001b[0m \u001b[31m63.8 MB/s\u001b[0m  \u001b[33m0:00:02\u001b[0m\n",
            "\u001b[?25hDownloading multimethod-1.12-py3-none-any.whl (10 kB)\n",
            "Downloading nlopt-2.11.0-cp313-cp313-manylinux_2_24_x86_64.manylinux_2_28_x86_64.whl (402 kB)\n",
            "Downloading ezdxf-1.4.5-cp313-cp313-manylinux2014_x86_64.manylinux_2_17_x86_64.whl (6.1 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.1/6.1 MB\u001b[0m \u001b[31m101.3 MB/s\u001b[0m  \u001b[33m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading casadi-3.8.2-cp311-abi3-manylinux_2_28_x86_64.whl (93.2 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m93.2/93.2 MB\u001b[0m \u001b[31m49.7 MB/s\u001b[0m  \u001b[33m0:00:01\u001b[0m\n",
            "\u001b[?25hDownloading runtype-0.5.3-py3-none-any.whl (31 kB)\n",
            "Downloading trame-4.0.0-py3-none-any.whl (27 kB)\n",
            "Downloading trame_client-4.1.4-py3-none-any.whl (568 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m568.3/568.3 kB\u001b[0m \u001b[31m22.5 MB/s\u001b[0m  \u001b[33m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading trame_common-1.3.0-py3-none-any.whl (36 kB)\n",
            "Downloading trame_server-4.1.3-py3-none-any.whl (55 kB)\n",
            "Downloading wslink-2.6.0-py3-none-any.whl (37 kB)\n",
            "Downloading trame_components-2.5.0-py3-none-any.whl (82 kB)\n",
            "Downloading trame_vtk-2.11.17-py3-none-any.whl (851 kB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m852.0/852.0 kB\u001b[0m \u001b[31m35.2 MB/s\u001b[0m  \u001b[33m0:00:00\u001b[0m\n",
            "\u001b[?25hDownloading trame_vuetify-3.3.0-py3-none-any.whl (6.8 MB)\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m6.8/6.8 MB\u001b[0m \u001b[31m75.8 MB/s\u001b[0m  \u001b[33m0:00:00\u001b[0m\n",
            "\u001b[?25hInstalling collected packages: trame-common, runtype, nlopt, multimethod, ezdxf, casadi, cadquery-ocp-proxy, trame-client, wslink, vtk, trame-vuetify, trame-vtk, trame-components, trame-server, cadquery-ocp, trame, cadquery\n",
            "\u001b[2K   \u001b[90m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━\u001b[0m \u001b[32m17/17\u001b[0m [cadquery]\n",
            "\u001b[1A\u001b[2KSuccessfully installed cadquery-2.8.0 cadquery-ocp-7.9.3.1.1 cadquery-ocp-proxy-7.9.3.1.1 casadi-3.8.2 ezdxf-1.4.5 multimethod-1.12 nlopt-2.11.0 runtype-0.5.3 trame-4.0.0 trame-client-4.1.4 trame-common-1.3.0 trame-components-2.5.0 trame-server-4.1.3 trame-vtk-2.11.17 trame-vuetify-3.3.0 vtk-9.6.2 wslink-2.6.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from dataclasses import dataclass\n",
        "from cadquery import func as cf\n",
        "\n",
        "@dataclass\n",
        "class CellSpec:\n",
        "    r_cell: float\n",
        "    h_cell: float\n",
        "\n",
        "def make_cell(spec):\n",
        "    return cf.cylinder(d=2 * spec.r_cell, h=spec.h_cell)\n",
        "\n",
        "def tray(spec, n=3, clearance=0.3, wall=4.0, thickness=6.0, depth=3.0):\n",
        "    pocket_r = spec.r_cell + clearance\n",
        "    pitch = 2 * pocket_r + wall\n",
        "\n",
        "    plate = cf.box(\n",
        "        n * pitch + wall,\n",
        "        2 * pocket_r + 2 * wall,\n",
        "        thickness\n",
        "    )\n",
        "\n",
        "    pocket = cf.cylinder(d=2 * pocket_r, h=depth + 1).moved(\n",
        "        z=thickness - depth\n",
        "    )\n",
        "\n",
        "    for i in range(n):\n",
        "        plate = plate - pocket.moved(\n",
        "            x=(i - (n - 1) / 2) * pitch\n",
        "        )\n",
        "\n",
        "    return plate\n",
        "\n",
        "cells = {\n",
        "    \"18650\": CellSpec(9.0, 65.0),\n",
        "    \"21700\": CellSpec(10.5, 70.0),\n",
        "    \"4680\": CellSpec(23.0, 80.0),\n",
        "}\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    for name, spec in cells.items():\n",
        "        t = tray(spec)\n",
        "        print(name, t.isValid(), round(t.Volume(), 1))\n",
        "        t.exportStl(f\"tray_{name}.stl\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "FA22jFO3n0ay",
        "outputId": "95af4da2-7143-4406-f03b-c140e5131061"
      },
      "execution_count": 3,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "18650 True 9013.8\n",
            "21700 True 11052.2\n",
            "4680 True 35690.2\n"
          ]
        }
      ]
    }
  ]
}