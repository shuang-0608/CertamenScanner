{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
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
        "<a href=\"https://colab.research.google.com/github/shuang-0608/CertamenScanner/blob/main/__init__.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ytChL4sJduSN",
        "outputId": "df8c650c-cef4-4b76-9683-08cddaa18442"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Mounted at /content/drive\n"
          ]
        }
      ],
      "source": [
        "from google.colab import drive\n",
        "drive.mount('/content/drive')"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "import PyPDF2\n",
        "import random\n",
        "import re\n",
        "\n",
        "pdf_path = '/content/drive/My Drive/Certamen_Sets/SampleSet.pdf'\n",
        "\n",
        "def extract_text_from_pdf(pdf_path):\n",
        "    pdf_reader = PyPDF2.PdfReader(open(pdf_path, 'rb'))\n",
        "    text = ''\n",
        "    for page in range(len(pdf_reader.pages)):\n",
        "        text += pdf_reader.pages[page].extract_text()\n",
        "    return text.replace('\\n', ' ')\n",
        "\n",
        "def parse_certamen_problems(text):\n",
        "    problems = re.split(r'\\d+\\.?\\s', text)[1:]\n",
        "    formatted_problems = []\n",
        "    for problem in problems:\n",
        "        toss_up_match = re.search(r'^(.*?)\\(?[A-Z]+\\.?\\)?\\sB1:', problem, re.DOTALL)\n",
        "        bonus1_match = re.search(r'B1:\\s(.*?)\\(?[A-Z]+\\.?\\)?\\sB2:', problem, re.DOTALL)\n",
        "        bonus2_match = re.search(r'B2:\\s(.*?)(?:\\(?[A-Z]+\\.?\\)?\\s|$)', problem, re.DOTALL)\n",
        "\n",
        "        if toss_up_match and bonus1_match and bonus2_match:\n",
        "            toss_up = toss_up_match.group(1)\n",
        "            bonus1 = bonus1_match.group(1)\n",
        "            bonus2 = bonus2_match.group(1)\n",
        "\n",
        "            toss_up = re.sub(r'\\(?[A-Z]+\\.?\\)?', '', toss_up)\n",
        "            bonus1 = re.sub(r'\\(?[A-Z]+\\.?\\)?', '', bonus1)\n",
        "            bonus2 = re.sub(r'\\(?[A-Z]+\\.?\\)?', '', bonus2)\n",
        "\n",
        "            formatted_problems.append({\n",
        "                'toss_up': toss_up.strip(),\n",
        "                'bonus1': bonus1.strip(),\n",
        "                'bonus2': bonus2.strip()\n",
        "            })\n",
        "    return formatted_problems\n",
        "\n",
        "def certamen_session(problems):\n",
        "    if not problems:\n",
        "        print(\"No Certamen problems found in the PDF.\")\n",
        "        return\n",
        "\n",
        "    problem = random.choice(problems)\n",
        "    print(\"Toss-Up Question:\")\n",
        "    print(problem['toss_up'])\n",
        "    input(\"Your answer: \")\n",
        "\n",
        "pdf_text = extract_text_from_pdf(pdf_path)\n",
        "\n",
        "certamen_problems = parse_certamen_problems(pdf_text)\n",
        "\n",
        "certamen_session(certamen_problems)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "og_rHWRLeI2a",
        "outputId": "18b76828-ca75-40eb-f8aa-b58989b6d5be"
      },
      "execution_count": 21,
      "outputs": [
        {
          "name": "stdout",
          "output_type": "stream",
          "text": [
            "Toss-Up Question:\n",
            "uod perīculum iuvenēs in viā obiērunt?   Ō / Ē Ō 3: hen recognized by the moderator, perform the following command or describe the actions you are being asked to perform: anibus sublātīs, stā in ūnō pede.\n",
            "Your answer: hi\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "def quiz_questions(questions):\n",
        "    for question in questions:\n",
        "        print(question)\n",
        "        user_answer = input(\"Your answer (in all capital letters): \")\n",
        "        print(\"\\n\")\n",
        "        # You can add logic to check correctness of the answer here if needed\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    quiz_set = [\n",
        "        \"1: The fabulae praetextae Romulus and Clastidium were written by what Latin author, who more famously composed a Bellum Punicum?\\n(CN.) NAEVIUS\",\n",
        "        \"B1: What powerful Roman family did Naevius attack in his verses?\\nMETELLI\",\n",
        "        \"B2: In what meter was the Bellum Punicum written?\\nSATURNIAN (VERSE) // SATURNIANS\",\n",
        "        \"2: Listen to the following passage, which I will read twice, then respondē Latīnē to the questions that follow: Sōle orientī, duae iuvenēs ē casā ēgressae sunt. Eīs māne proficīscendum erat ut longum iter ante noctem perficerent. Nōndum duās hōrās ambulāverant ubi prīma iuvenis exclāmāvit, “Amīca! Cōnsiste! Gregem canum ferōrum nōbīs appropinquantem videō! Quōmodo nōs servāre possumus?” secunda iuvenis, quae multō fortior quam comes erat, cultrum dēstrīnxit et canibus advertit.\\nquandō iuvenēs ē casā ēgressae sunt?\\nSŌLE ORIENTĪ / MĀNE / PRIMĀ LUCE\",\n",
        "        \"B1. Cūr necesse erat iuvenibus māne proficīscī?\\nUT (LONGUM) ITER (ANTE NOCTEM) PERFICERENT / QUOD ITER ERAT LONGUM\",\n",
        "        \"B2. Quod perīculum iuvenēs in viā obiērunt?\\nGREGEM CANUM (FERŌRUM) / CANĒS (FERŌS)\",\n",
        "        \"3: When recognized by the moderator, perform the following command or describe the actions you are being asked to perform: Manibus sublātīs, stā in ūnō pede.\\nSTUDENT STANDS ON ONE FOOT WITH HANDS RAISED IN THE AIR.\",\n",
        "        \"B1: Ūnō pede in sellā, alterō humī positō, circumspectā et dīc Anglicē, “Ego sum dux patriae.”\\nWITH ONE FOOT ON THE CHAIR AND THE OTHER ON THE GROUND, ONE STUDENT LOOKS AROUND AND SAYS IN ENGLISH, “I AM THE LEADER OF THE / MY COUNTRY.”\",\n",
        "        \"B2: Aurēs digitīs tangentēs, dīcite Anglicē, “Vōs audīre nōn possumus.”\\nWITH FINGERS IN / ON EARS, AT LEAST TWO STUDENTS SAY “WE CAN’T HEAR YOU.”\",\n",
        "        \"4: What group, while they were on an island called “Bear Mountain,” found six-armed earthborn monsters, met the king Cyzicus, heeded Mopsus’ prophecies, and obeyed Jason’s orders?\\n(THE) ARGONAUTS / MINYANS\",\n",
        "        \"B1: What actual mountain, sacred to the goddess Cybele, stood on the island “Bear Mountain” and was the site of propitiatory sacrifices by the Argonauts? (MOUNT) DINDYMUS / DINDYMON\",\n",
        "        \"B2: To learn that the Argonauts needed to propitiate Cybele, the seer Mopsus interpreted the cries of what bird, into which Ceÿx was transformed in another story?\\nKINGFISHER / HALCYON (BIRD)\",\n",
        "        \"5: What general — together with his older brother, who was nicknamed Calvus — won his greatest victory at Dertosa before dying at the Upper Baetis river in 211 BC, leaving command to his son, Scipio Africanus?\\nPUBLIUS (CORNELIUS) SCIPIO (THE ELDER)\",\n",
        "        \"B1: Where did the younger Scipio save his father’s life in battle in 218 BC in one of the opening skirmishes of the war?\\nTICINUS RIVER\",\n",
        "        \"B2: Sc\" ]\n",
        "\n",
        "quiz_questions(quiz_set)"
      ],
      "metadata": {
        "id": "KG9X9-8SvqqF",
        "outputId": "688a797c-b94b-4c94-cf74-81dc7bdee4b3",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        }
      },
      "execution_count": 23,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "1: The fabulae praetextae Romulus and Clastidium were written by what Latin author, who more famously composed a Bellum Punicum?\n",
            "(CN.) NAEVIUS\n",
            "Your answer (in all capital letters): hi\n",
            "\n",
            "\n",
            "B1: What powerful Roman family did Naevius attack in his verses?\n",
            "METELLI\n",
            "Your answer (in all capital letters): okay\n",
            "\n",
            "\n",
            "B2: In what meter was the Bellum Punicum written?\n",
            "SATURNIAN (VERSE) // SATURNIANS\n",
            "Your answer (in all capital letters): no\n",
            "\n",
            "\n",
            "2: Listen to the following passage, which I will read twice, then respondē Latīnē to the questions that follow: Sōle orientī, duae iuvenēs ē casā ēgressae sunt. Eīs māne proficīscendum erat ut longum iter ante noctem perficerent. Nōndum duās hōrās ambulāverant ubi prīma iuvenis exclāmāvit, “Amīca! Cōnsiste! Gregem canum ferōrum nōbīs appropinquantem videō! Quōmodo nōs servāre possumus?” secunda iuvenis, quae multō fortior quam comes erat, cultrum dēstrīnxit et canibus advertit.\n",
            "quandō iuvenēs ē casā ēgressae sunt?\n",
            "SŌLE ORIENTĪ / MĀNE / PRIMĀ LUCE\n",
            "Your answer (in all capital letters): fine\n",
            "\n",
            "\n",
            "B1. Cūr necesse erat iuvenibus māne proficīscī?\n",
            "UT (LONGUM) ITER (ANTE NOCTEM) PERFICERENT / QUOD ITER ERAT LONGUM\n",
            "Your answer (in all capital letters): alright\n",
            "\n",
            "\n",
            "B2. Quod perīculum iuvenēs in viā obiērunt?\n",
            "GREGEM CANUM (FERŌRUM) / CANĒS (FERŌS)\n",
            "Your answer (in all capital letters): bruh\n",
            "\n",
            "\n",
            "3: When recognized by the moderator, perform the following command or describe the actions you are being asked to perform: Manibus sublātīs, stā in ūnō pede.\n",
            "STUDENT STANDS ON ONE FOOT WITH HANDS RAISED IN THE AIR.\n",
            "Your answer (in all capital letters): bad\n",
            "\n",
            "\n",
            "B1: Ūnō pede in sellā, alterō humī positō, circumspectā et dīc Anglicē, “Ego sum dux patriae.”\n",
            "WITH ONE FOOT ON THE CHAIR AND THE OTHER ON THE GROUND, ONE STUDENT LOOKS AROUND AND SAYS IN ENGLISH, “I AM THE LEADER OF THE / MY COUNTRY.”\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "Interrupted by user",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-23-706a93ac0fda>\u001b[0m in \u001b[0;36m<cell line: 26>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     24\u001b[0m         \"B2: Sc\" ]\n\u001b[1;32m     25\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 26\u001b[0;31m \u001b[0mquiz_questions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mquiz_set\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m<ipython-input-23-706a93ac0fda>\u001b[0m in \u001b[0;36mquiz_questions\u001b[0;34m(questions)\u001b[0m\n\u001b[1;32m      2\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mquestion\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mquestions\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      3\u001b[0m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mquestion\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m----> 4\u001b[0;31m         \u001b[0muser_answer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Your answer (in all capital letters): \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m      5\u001b[0m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"\\n\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m      6\u001b[0m         \u001b[0;31m# You can add logic to check correctness of the answer here if needed\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m    849\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    850\u001b[0m             )\n\u001b[0;32m--> 851\u001b[0;31m         return self._input_request(str(prompt),\n\u001b[0m\u001b[1;32m    852\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    853\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    893\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    894\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 895\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    896\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    897\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "!pip install PyMuPDF\n",
        "import fitz\n",
        "def extract_text_from_pdf(pdf_path):\n",
        "    doc = fitz.open(pdf_path)\n",
        "    text = \"\"\n",
        "    for page in doc:\n",
        "        text += page.get_text()\n",
        "    return text\n",
        "\n",
        "def quiz_questions_from_pdf(pdf_path):\n",
        "    pdf_text = extract_text_from_pdf(pdf_path)\n",
        "    questions = pdf_text.split(\"\\n\\n\")\n",
        "    return questions\n",
        "\n",
        "def quiz_questions(questions):\n",
        "    for question in questions:\n",
        "        print(question)\n",
        "        user_answer = input(\"Your answer (in all capital letters): \")\n",
        "        print(\"\\n\")\n",
        "        # You can add logic to check correctness of the answer here if needed\n",
        "\n",
        "if __name__ == \"__main__\":\n",
        "    pdf_path = '/content/drive/My Drive/Certamen_Sets/SampleSet.pdf'  # Replace with the actual path\n",
        "    quiz_set = quiz_questions_from_pdf(pdf_path)\n",
        "    quiz_questions(quiz_set)"
      ],
      "metadata": {
        "id": "Jb3hi2HgxFJC",
        "outputId": "7c9e5333-0a0c-43cf-a7fa-a389aea0fcbf",
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 1000
        }
      },
      "execution_count": 26,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Requirement already satisfied: PyMuPDF in /usr/local/lib/python3.10/dist-packages (1.24.8)\n",
            "Requirement already satisfied: PyMuPDFb==1.24.8 in /usr/local/lib/python3.10/dist-packages (from PyMuPDF) (1.24.8)\n",
            "1: The fabulae praetextae Romulus and Clastidium were written by what Latin author, who\n",
            "more famously composed a Bellum Punicum?\n",
            "(CN.) NAEVIUS\n",
            "B1: What powerful Roman family did Naevius attack in his verses?\n",
            "METELLI\n",
            "B2: In what meter was the Bellum Punicum written?\n",
            "SATURNIAN (VERSE) // SATURNIANS\n",
            "2: Listen to the following passage, which I will read twice, then respondē Latīnē to the\n",
            "questions that follow: Sōle orientī, duae iuvenēs ē casā ēgressae sunt. Eīs māne\n",
            "proficīscendum erat ut longum iter ante noctem perficerent. Nōndum duās hōrās\n",
            "ambulāverant ubi prīma iuvenis exclāmāvit, “Amīca! Cōnsiste! Gregem canum ferōrum nōbīs\n",
            "appropinquantem videō! Quōmodo nōs servāre possumus?” secunda iuvenis, quae multō\n",
            "fortior quam comes erat, cultrum dēstrīnxit et canibus advertit.\n",
            "quandō iuvenēs ē casā ēgressae sunt?\n",
            "SŌLE ORIENTĪ / MĀNE / PRIMĀ LUCE\n",
            "B1. Cūr necesse erat iuvenibus māne proficīscī?\n",
            "UT (LONGUM) ITER (ANTE NOCTEM) PERFICERENT / QUOD ITER ERAT LONGUM\n",
            "B2. Quod perīculum iuvenēs in viā obiērunt?\n",
            "GREGEM CANUM (FERŌRUM) / CANĒS (FERŌS)\n",
            "3: When recognized by the moderator, perform the following command or describe the\n",
            "actions you are being asked to perform: Manibus sublātīs, stā in ūnō pede.\n",
            "STUDENT STANDS ON ONE FOOT WITH HANDS RAISED IN THE AIR.\n",
            "B1: Ūnō pede in sellā, alterō humī positō, circumspectā et dīc Anglicē, “Ego sum dux\n",
            "patriae.”\n",
            "WITH ONE FOOT ON THE CHAIR AND THE OTHER ON THE GROUND, ONE STUDENT\n",
            "LOOKS AROUND AND SAYS IN ENGLISH, “I AM THE LEADER OF THE / MY COUNTRY.”\n",
            "B2: Aurēs digitīs tangentēs, dīcite Anglicē, “Vōs audīre nōn possumus.”\n",
            "WITH FINGERS IN / ON EARS, AT LEAST TWO STUDENTS SAY “WE CAN’T HEAR\n",
            "YOU.”\n",
            "4: What group, while they were on an island called “Bear Mountain,” found six-armed\n",
            "earthborn monsters, met the king Cyzicus, heeded Mopsus’ prophecies, and obeyed Jason’s\n",
            "orders?\n",
            "(THE) ARGONAUTS / MINYANS\n",
            "B1: What actual mountain, sacred to the goddess Cybele, stood on the island “Bear\n",
            "Mountain” and was the site of propitiatory sacrifices by the Argonauts? (MOUNT)\n",
            "DINDYMUS / DINDYMON\n",
            "B2: To learn that the Argonauts needed to propitiate Cybele, the seer Mopsus interpreted the\n",
            "cries of what bird, into which Ceÿx was transformed in another story?\n",
            "KINGFISHER / HALCYON (BIRD)\n",
            "5: What general — together with his older brother, who was nicknamed Calvus — won his\n",
            "greatest victory at Dertosa before dying at the Upper Baetis river in 211 BC, leaving\n",
            "command to his son, Scipio Africanus?\n",
            "PUBLIUS (CORNELIUS) SCIPIO (THE ELDER)\n",
            "B1: Where did the younger Scipio save his father’s life in battle in 218 BC in one of the\n",
            "opening skirmishes of the war?\n",
            "TICINUS RIVER\n",
            "B2: Scipio Africanus later took what city in Hispania in 209 BC by attacking over a lagoon?\n",
            "CARTHĀGŌ NOVA / NEW CARTHAGE\n",
            "\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "Interrupted by user",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-26-17b5f20779c6>\u001b[0m in \u001b[0;36m<cell line: 22>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     23\u001b[0m     \u001b[0mpdf_path\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0;34m'/content/drive/My Drive/Certamen_Sets/SampleSet.pdf'\u001b[0m  \u001b[0;31m# Replace with the actual path\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     24\u001b[0m     \u001b[0mquiz_set\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0mquiz_questions_from_pdf\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mpdf_path\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 25\u001b[0;31m     \u001b[0mquiz_questions\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mquiz_set\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m<ipython-input-26-17b5f20779c6>\u001b[0m in \u001b[0;36mquiz_questions\u001b[0;34m(questions)\u001b[0m\n\u001b[1;32m     16\u001b[0m     \u001b[0;32mfor\u001b[0m \u001b[0mquestion\u001b[0m \u001b[0;32min\u001b[0m \u001b[0mquestions\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     17\u001b[0m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0mquestion\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 18\u001b[0;31m         \u001b[0muser_answer\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Your answer (in all capital letters): \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     19\u001b[0m         \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"\\n\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     20\u001b[0m         \u001b[0;31m# You can add logic to check correctness of the answer here if needed\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m    849\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    850\u001b[0m             )\n\u001b[0;32m--> 851\u001b[0;31m         return self._input_request(str(prompt),\n\u001b[0m\u001b[1;32m    852\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    853\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    893\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    894\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 895\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    896\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    897\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ]
    }
  ]
}