valid_creds = [
{
  "text": "string"
},
{
  "text": "hghjghgj jhkjh 675765 &^&*^% khkhkhkjhkj"
},
{
  "text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem "
          "Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown"
          " printer took a galley of type and scrambled it to make a type specimen book. It has survived"
          " not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged."
          " It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and "
          "more recently with desktopuu"
}
]

invalid_creds = [
{
  "text": "",
  "expected_error": "A quick message can’t be empty"
},
{
  "text": "     ",
  "expected_error": "A quick message can’t be empty"
},
{
  "text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's"
          " standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a"
          " type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining "
          "essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and "
          "more recently with desktopt Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the "
          "industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type "
          "specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. "
          "It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktopttq",
  "expected_error": "Text length must be between 1 and 1000 characters"
}
]

valid_creds_for_updating = [
{
  "id": 490,
  "text": "string"
},
{
  "id": 490,
  "text": "hghjghgj jhkjh 675765 &^&*^% khkhkhkjhkj"
},
{
  "id": 490,
  "text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's "
          "standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make "
          "a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining"
          " essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem "
          "Ipsum passages, and more recently with desktopuu"
}
]

invalid_creds_for_updating = [
{
  "id": 490,
  "text": "",
  "expected_error": "A quick message can’t be empty"
},
{
  "id": 490,
  "text": "    ",
  "expected_error": "A quick message can’t be empty"
},
{
  "id": 490,
  "text": "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the"
          " industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and"
          " scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into "
          "electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of "
          "Letraset sheets containing Lorem Ipsum passages, and more recently with desktopt Lorem Ipsum is simply dummy text "
          "of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, "
          "when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five "
          "centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s "
          "with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktopttq",
  "expected_error": "Text length must be between 1 and 1000 characters"
}
]

