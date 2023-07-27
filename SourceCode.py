#!/usr/bin/env python
# coding: utf-8

# In[3]:


from translate import Translator
import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

from googletrans import Translator as GoogleTranslator

def translate_text(input_text, dest_lang):
    translator = GoogleTranslator()
    translated_text = translator.translate(input_text, dest=dest_lang)
    return translated_text.text

def translate_button_clicked(input_text_area, dest_lang_combo, output_text_area, lang_codes_to_names):
    input_text = input_text_area.get("1.0", tk.END).strip()
    dest_lang = dest_lang_combo.get()

    if not input_text:
        messagebox.showerror("Error", "Please enter the text to translate.")
        return

    if not dest_lang:
        messagebox.showerror("Error", "Please select the destination language.")
        return

    dest_lang_code = next((code for code, name in lang_codes_to_names.items() if name == dest_lang), None)

    try:
        translated_text = translate_text(input_text, dest_lang_code)
        output_text_area.delete("1.0", tk.END)
        output_text_area.insert(tk.END, translated_text)
    except Exception as e:
        messagebox.showerror("Error", f"Translation failed: {str(e)}")



def main():
    lang_codes_to_names = {
        'ar': 'Arabic',
        'bg': 'Bulgarian',
        'bn': 'Bengali',    
        'cs': 'Czech',
        'da': 'Danish',
        'de': 'German',
        'el': 'Greek',
        'en': 'English',
        'es': 'Spanish',
        'et': 'Estonian',
        'fa': 'Persian',
        'fi': 'Finnish',
        'fr': 'French',
        'gu': 'Gujarati',   
        'he': 'Hebrew',
        'hi': 'Hindi',
        'hr': 'Croatian',
        'hu': 'Hungarian',
        'hy': 'Armenian',
        'id': 'Indonesian',
        'it': 'Italian',
        'ja': 'Japanese',
        'ka': 'Georgian',
        'kk': 'Kazakh',
        'kn': 'Kannada',    
        'ko': 'Korean',
        'lt': 'Lithuanian',
        'lv': 'Latvian',
        'mk': 'Macedonian',
        'ml': 'Malayalam',
        'mr': 'Marathi',
        'ms': 'Malay',
        'nl': 'Dutch',
        'no': 'Norwegian',
        'pa': 'Punjabi',   
        'pl': 'Polish',
        'pt': 'Portuguese',
        'ro': 'Romanian',
        'ru': 'Russian',
        'sk': 'Slovak',
        'sl': 'Slovenian',
        'sq': 'Albanian',
        'sr': 'Serbian',
        'sv': 'Swedish',
        'ta': 'Tamil',      
        'te': 'Telugu',     
        'th': 'Thai',
        'tr': 'Turkish',
        'uk': 'Ukrainian',
        'ur': 'Urdu',       
        'uz': 'Uzbek',
        'vi': 'Vietnamese',
        'zh-CN': 'Chinese-Simplified',
    }

    root = tk.Tk()
    root.title("Text Translator")

    main_frame = ttk.Frame(root, padding="10")
    main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

    input_text_area = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=40, height=10)
    input_text_area.grid(row=0, column=0, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))

    dest_lang_label = ttk.Label(main_frame, text="Destination Language:")
    dest_lang_label.grid(row=1, column=0, padx=5, pady=5, sticky=tk.W)

    dest_lang_var = tk.StringVar()
    dest_lang_combo = ttk.Combobox(main_frame, textvariable=dest_lang_var, width=15, values=sorted(lang_codes_to_names.values()))
    dest_lang_combo.grid(row=1, column=1, padx=5, pady=5, sticky=tk.W)
    dest_lang_combo.set('English')  # Set the default language

    translate_button = ttk.Button(main_frame, text="Translate", command=lambda: translate_button_clicked(input_text_area, dest_lang_combo, output_text_area, lang_codes_to_names))
    translate_button.grid(row=2, column=0, columnspan=2, padx=5, pady=5)

    output_text_area = scrolledtext.ScrolledText(main_frame, wrap=tk.WORD, width=40, height=10)
    output_text_area.grid(row=3, column=0, columnspan=2, padx=5, pady=5, sticky=(tk.W, tk.E, tk.N, tk.S))

    root.mainloop()

if __name__ == "__main__":
    main()


# In[ ]:




