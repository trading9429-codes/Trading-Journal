with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/apply_v18_uiux_overhaul.py", "r", encoding="utf-8") as f:
    lines = f.readlines()

lines[100] = '    old_style_target = "      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.4);\\n    }\\n\\n    }\\n  </style>\\n</head>\'\'\'"\n'
lines[101] = '    assert old_style_target in code, "Failed to find old_style_target"\n'
lines[102] = '    code = code.replace(old_style_target, "      box-shadow: 0 1px 2px rgba(0, 0, 0, 0.4);\\n    }\\n" + uiux_css + "\\n    }\\n  </style>\\n</head>\'\'\'", 1)\n'

with open("/home/sunny/.gemini/antigravity/scratch/trader-reset-system/apply_v18_uiux_overhaul.py", "w", encoding="utf-8") as f:
    f.writelines(lines)

print("Updated style target in apply_v18_uiux_overhaul.py")
