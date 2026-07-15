# Copyright (C) 2026 AnkiCraft
# This file is part of Always on Top (by Ankicraft).
# License: GNU AGPL v3 <https://www.gnu.org/licenses/agpl-3.0.html>

from __future__ import annotations

from functools import lru_cache

FALLBACK: str = "es"

TRANSLATIONS: dict[str, dict[str, str]] = {
    "en": {
        "shortcut_label": "Shortcut to keep Anki on top",
        "shortcut_prefix": "Shortcut:",
        "placeholder": "Press the keyboard shortcut",
        "save": "OK",
        "cancel": "Cancel",
        "defaults": "Restore defaults",
        "on": "Always on top: enabled",
        "off": "Always on top: disabled",
        "shortcut_updated": "Keyboard shortcut updated",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Buy me a coffee",
        "kofi_tooltip": "Support AnkiCraft on Ko-fi",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d Rate this add-on",
        "report_button": "Report a bug",
        "welcome_close": "Close",
        "welcome_body": (
            "Always on Top pins the Add Card window above all other windows "
            "on your screen — so you can keep adding notes without switching back to Anki.\n\n"
            "Press your configured shortcut (default: Ctrl+Shift+T) to toggle it on or off. "
            "Change it any time via Tools → Add-ons → {name} → Config."
        ),
        "welcome_support_note": (
            "This add-on is free and open source (AGPLv3). "
            "If it saves you time, consider supporting its development!"
        ),
    },
    "es": {
        "shortcut_label": "Atajo para superponer Anki",
        "shortcut_prefix": "Atajo:",
        "placeholder": "Presione el atajo de teclado",
        "save": "Aceptar",
        "cancel": "Cancelar",
        "defaults": "Restaurar los valores predeterminados",
        "on": "Siempre visible: activado",
        "off": "Siempre visible: desactivado",
        "shortcut_updated": "Atajo de teclado actualizado",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Ko-fi",
        "kofi_tooltip": "Apoya a AnkiCraft en Ko-fi",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d Valorar este complemento",
        "report_button": "Reportar un error",
        "welcome_close": "Cerrar",
        "welcome_body": (
            "Siempre visible fija la ventana de Añadir tarjeta sobre todas las demás "
            "ventanas — para que puedas seguir añadiendo notas sin cambiar de ventana.\n\n"
            "Usa tu atajo configurado (predeterminado: Ctrl+Shift+T) para activarlo o desactivarlo. "
            "Cámbialo cuando quieras en Herramientas → Complementos → {name} → Configuración."
        ),
        "welcome_support_note": (
            "Este complemento es gratuito y de código abierto (AGPLv3). "
            "¡Si te ahorra tiempo, considera apoyar su desarrollo!"
        ),
    },
    "fr": {
        "shortcut_label": "Raccourci pour garder Anki au premier plan",
        "shortcut_prefix": "Raccourci :",
        "placeholder": "Appuyez sur le raccourci clavier",
        "save": "Accepter",
        "cancel": "Annuler",
        "defaults": "Restaurer les valeurs par défaut",
        "on": "Toujours au premier plan : activé",
        "off": "Toujours au premier plan : désactivé",
        "shortcut_updated": "Raccourci clavier mis à jour",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Ko-fi",
        "kofi_tooltip": "Soutenez AnkiCraft sur Ko-fi",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d Évaluer cette extension",
        "report_button": "Signaler un bug",
        "welcome_close": "Fermer",
        "welcome_body": (
            "Always on Top épingle la fenêtre d’ajout de cartes au-dessus de toutes les autres "
            "— vous pouvez ainsi continuer à ajouter des notes sans revenir constamment sur Anki.\n\n"
            "Appuyez sur votre raccourci configuré (par défaut : Ctrl+Shift+T) pour l’activer ou le désactiver. "
            "Modifiez-le à tout moment via Outils → Extensions → {name} → Config."
        ),
        "welcome_support_note": (
            "Cette extension est gratuite et open source (AGPLv3). "
            "Si elle vous fait gagner du temps, pensez à soutenir son développement !"
        ),
    },
    "de": {
        "shortcut_label": "Tastenkürzel, um Anki im Vordergrund zu halten",
        "shortcut_prefix": "Tastenkürzel:",
        "placeholder": "Drücken Sie die Tastenkombination",
        "save": "OK",
        "cancel": "Abbrechen",
        "defaults": "Standardwerte wiederherstellen",
        "on": "Immer im Vordergrund: aktiviert",
        "off": "Immer im Vordergrund: deaktiviert",
        "shortcut_updated": "Tastenkombination aktualisiert",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Ko-fi",
        "kofi_tooltip": "Unterstütze AnkiCraft auf Ko-fi",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d Dieses Add-on bewerten",
        "report_button": "Fehler melden",
        "welcome_close": "Schließen",
        "welcome_body": (
            "Always on Top heftet das Karten-Hinzufügen-Fenster über alle anderen Fenster "
            "— damit du weiter Notizen hinzufügen kannst, ohne ständig zu Anki zurückzuwechseln.\n\n"
            "Drücke dein konfiguriertes Tastenkürzel (Standard: Ctrl+Shift+T), um es ein- oder auszuschalten. "
            "Ändere es jederzeit unter Werkzeuge → Add-ons → {name} → Konfiguration."
        ),
        "welcome_support_note": (
            "Dieses Add-on ist kostenlos und Open Source (AGPLv3). "
            "Wenn es dir Zeit spart, erwäge die Unterstützung seiner Entwicklung!"
        ),
    },
    "it": {
        "shortcut_label": "Scorciatoia per tenere Anki in primo piano",
        "shortcut_prefix": "Scorciatoia:",
        "placeholder": "Premi la scorciatoia da tastiera",
        "save": "Accetta",
        "cancel": "Annulla",
        "defaults": "Ripristina i valori predefiniti",
        "on": "Sempre in primo piano: attivato",
        "off": "Sempre in primo piano: disattivato",
        "shortcut_updated": "Scorciatoia da tastiera aggiornata",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Ko-fi",
        "kofi_tooltip": "Supporta AnkiCraft su Ko-fi",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d Valuta questo componente",
        "report_button": "Segnala un bug",
        "welcome_close": "Chiudi",
        "welcome_body": (
            "Always on Top fissa la finestra Aggiungi carta sopra tutte le altre finestre "
            "— così puoi continuare ad aggiungere note senza tornare costantemente su Anki.\n\n"
            "Premi la scorciatoia configurata (predefinita: Ctrl+Shift+T) per attivarlo o disattivarlo. "
            "Modificala in qualsiasi momento tramite Strumenti → Componenti aggiuntivi → {name} → Config."
        ),
        "welcome_support_note": (
            "Questo componente è gratuito e open source (AGPLv3). "
            "Se ti fa risparmiare tempo, considera di supportarne lo sviluppo!"
        ),
    },
    "pt_BR": {
        "shortcut_label": "Atalho para manter o Anki sempre visível",
        "shortcut_prefix": "Atalho:",
        "placeholder": "Pressione o atalho de teclado",
        "save": "Aceitar",
        "cancel": "Cancelar",
        "defaults": "Restaurar os valores padrão",
        "on": "Sempre visível: ativado",
        "off": "Sempre visível: desativado",
        "shortcut_updated": "Atalho de teclado atualizado",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Ko-fi",
        "kofi_tooltip": "Apoie o AnkiCraft no Ko-fi",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d Avaliar este complemento",
        "report_button": "Reportar um bug",
        "welcome_close": "Fechar",
        "welcome_body": (
            "Always on Top fixa a janela de Adicionar Cartão acima de todas as outras janelas "
            "— para que você possa continuar adicionando notas sem precisar alternar de volta ao Anki.\n\n"
            "Pressione o atalho configurado (padrão: Ctrl+Shift+T) para ativar ou desativar. "
            "Altere-o a qualquer momento em Ferramentas → Complementos → {name} → Configurações."
        ),
        "welcome_support_note": (
            "Este complemento é gratuito e de código aberto (AGPLv3). "
            "Se ele economiza seu tempo, considere apoiar seu desenvolvimento!"
        ),
    },
    "pt_PT": {
        "shortcut_label": "Atalho para manter o Anki sempre visível",
        "shortcut_prefix": "Atalho:",
        "placeholder": "Prima o atalho de teclado",
        "save": "Aceitar",
        "cancel": "Cancelar",
        "defaults": "Restaurar os valores predefinidos",
        "on": "Sempre visível: ativado",
        "off": "Sempre visível: desativado",
        "shortcut_updated": "Atalho de teclado atualizado",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Ko-fi",
        "kofi_tooltip": "Apoie o AnkiCraft no Ko-fi",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d Avaliar este complemento",
        "report_button": "Reportar um erro",
        "welcome_close": "Fechar",
        "welcome_body": (
            "Always on Top fixa a janela de Adicionar Cartão acima de todas as outras "
            "— para que possa continuar a adicionar notas sem precisar voltar ao Anki.\n\n"
            "Prima o atalho configurado (predefinido: Ctrl+Shift+T) para ativar ou desativar. "
            "Altere-o a qualquer momento em Ferramentas → Extensões → {name} → Config."
        ),
        "welcome_support_note": (
            "Este complemento é gratuito e de código aberto (AGPLv3). "
            "Se lhe poupa tempo, considere apoiar o seu desenvolvimento!"
        ),
    },
    "nl": {
        "shortcut_label": "Sneltoets om Anki op de voorgrond te houden",
        "shortcut_prefix": "Sneltoets:",
        "placeholder": "Druk op de sneltoets",
        "save": "Accepteren",
        "cancel": "Annuleren",
        "defaults": "Standaardwaarden herstellen",
        "on": "Altijd op de voorgrond: ingeschakeld",
        "off": "Altijd op de voorgrond: uitgeschakeld",
        "shortcut_updated": "Sneltoets bijgewerkt",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Ko-fi",
        "kofi_tooltip": "Ondersteun AnkiCraft op Ko-fi",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d Beoordeel deze add-on",
        "report_button": "Een bug melden",
        "welcome_close": "Sluiten",
        "welcome_body": (
            "Always on Top zet het venster Kaart toevoegen boven alle andere vensters "
            "— zodat je door kunt gaan met notities toevoegen zonder steeds terug te schakelen naar Anki.\n\n"
            "Druk op je ingestelde sneltoets (standaard: Ctrl+Shift+T) om het in of uit te schakelen. "
            "Wijzig het op elk moment via Extra → Add-ons → {name} → Config."
        ),
        "welcome_support_note": (
            "Deze add-on is gratis en open source (AGPLv3). "
            "Als het je tijd bespaart, overweeg dan de ontwikkeling te ondersteunen!"
        ),
    },
    "ca": {"shortcut_label": "Drecera per mantenir l'Anki sempre visible", "shortcut_prefix": "Drecera:", "placeholder": "Premeu la drecera de teclat", "save": "Accepta", "cancel": "Cancel·la", "defaults": "Restaura els valors predeterminats", "on": "Sempre visible: activat", "off": "Sempre visible: desactivat", "shortcut_updated": "Drecera de teclat actualitzada"},
    "gl": {"shortcut_label": "Atallo para manter Anki sempre visible", "shortcut_prefix": "Atallo:", "placeholder": "Prema o atallo de teclado", "save": "Aceptar", "cancel": "Cancelar", "defaults": "Restaurar os valores predeterminados", "on": "Sempre visible: activado", "off": "Sempre visible: desactivado", "shortcut_updated": "Atallo de teclado actualizado"},
    "ro": {"shortcut_label": "Comandă rapidă pentru a menține Anki deasupra", "shortcut_prefix": "Comandă rapidă:", "placeholder": "Apăsați comanda rapidă de la tastatură", "save": "Acceptă", "cancel": "Anulează", "defaults": "Restabilește valorile implicite", "on": "Mereu deasupra: activat", "off": "Mereu deasupra: dezactivat", "shortcut_updated": "Comanda rapidă a fost actualizată"},
    "ru": {
        "shortcut_label": "Сочетание клавиш, чтобы держать Anki поверх окон",
        "shortcut_prefix": "Сочетание клавиш:",
        "placeholder": "Нажмите сочетание клавиш",
        "save": "Принять",
        "cancel": "Отмена",
        "defaults": "Восстановить значения по умолчанию",
        "on": "Поверх окон: включено",
        "off": "Поверх окон: выключено",
        "shortcut_updated": "Сочетание клавиш обновлено",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Ko-fi",
        "kofi_tooltip": "Поддержите AnkiCraft на Ko-fi",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d Оценить это дополнение",
        "report_button": "Сообщить об ошибке",
        "welcome_close": "Закрыть",
        "welcome_body": (
            "Always on Top закрепляет окно добавления карточек поверх всех остальных окон "
            "— чтобы вы могли продолжать добавлять заметки, не переключаясь обратно в Anki.\n\n"
            "Нажмите настроенное сочетание клавиш (по умолчанию: Ctrl+Shift+T), чтобы включить или выключить. "
            "Измените его в любое время через Инструменты → Дополнения → {name} → Конфигурация."
        ),
        "welcome_support_note": (
            "Это дополнение бесплатно и с открытым исходным кодом (AGPLv3). "
            "Если оно экономит ваше время, рассмотрите возможность поддержки его разработки!"
        ),
    },
    "uk": {
        "shortcut_label": "Комбінація клавіш, щоб тримати Anki зверху",
        "shortcut_prefix": "Комбінація клавіш:",
        "placeholder": "Натисніть комбінацію клавіш",
        "save": "Прийняти",
        "cancel": "Скасувати",
        "defaults": "Відновити типові значення",
        "on": "Завжди зверху: увімкнено",
        "off": "Завжди зверху: вимкнено",
        "shortcut_updated": "Комбінацію клавіш оновлено",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Ko-fi",
        "kofi_tooltip": "Підтримайте AnkiCraft на Ko-fi",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d Оцінити цей додаток",
        "report_button": "Повідомити про помилку",
        "welcome_close": "Закрити",
        "welcome_body": (
            "Always on Top закріплює вікно додавання карток поверх усіх інших вікон "
            "— щоб ви могли продовжувати додавати нотатки, не перемикаючись назад до Anki.\n\n"
            "Натисніть налаштоване поєднання клавіш (за замовчуванням: Ctrl+Shift+T), щоб увімкнути або вимкнути. "
            "Змініть його в будь-який час через Інструменти → Додатки → {name} → Конфігурація."
        ),
        "welcome_support_note": (
            "Цей додаток безкоштовний і з відкритим вихідним кодом (AGPLv3). "
            "Якщо він економить ваш час, розгляньте можливість підтримки його розробки!"
        ),
    },
    "pl": {
        "shortcut_label": "Skrót, aby trzymać Anki na wierzchu",
        "shortcut_prefix": "Skrót:",
        "placeholder": "Naciśnij skrót klawiszowy",
        "save": "Akceptuj",
        "cancel": "Anuluj",
        "defaults": "Przywróć wartości domyślne",
        "on": "Zawsze na wierzchu: włączone",
        "off": "Zawsze na wierzchu: wyłączone",
        "shortcut_updated": "Skrót klawiszowy zaktualizowany",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Ko-fi",
        "kofi_tooltip": "Wesprzyj AnkiCraft na Ko-fi",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d Oceń ten dodatek",
        "report_button": "Zgłoś błąd",
        "welcome_close": "Zamknij",
        "welcome_body": (
            "Always on Top przypina okno Dodaj kartę nad wszystkimi innymi oknami "
            "— dzięki temu możesz dalej dodawać notatki bez ciągłego przełączania się do Anki.\n\n"
            "Naciśnij skonfigurowany skrót (domyślnie: Ctrl+Shift+T), aby włączyć lub wyłączyć. "
            "Zmień go w dowolnym momencie w Narzędzia → Dodatki → {name} → Konfiguracja."
        ),
        "welcome_support_note": (
            "Ten dodatek jest darmowy i open source (AGPLv3). "
            "Jeśli oszczędza Twój czas, rozważ wsparcie jego rozwoju!"
        ),
    },
    "cs": {"shortcut_label": "Zkratka pro udržení Anki navrchu", "shortcut_prefix": "Zkratka:", "placeholder": "Stiskněte klávesovou zkratku", "save": "Přijmout", "cancel": "Zrušit", "defaults": "Obnovit výchozí hodnoty", "on": "Vždy navrchu: zapnuto", "off": "Vždy navrchu: vypnuto", "shortcut_updated": "Klávesová zkratka aktualizována"},
    "sk": {"shortcut_label": "Skratka na udržanie Anki navrchu", "shortcut_prefix": "Skratka:", "placeholder": "Stlačte klávesovú skratku", "save": "Prijať", "cancel": "Zrušiť", "defaults": "Obnoviť predvolené hodnoty", "on": "Vždy navrchu: zapnuté", "off": "Vždy navrchu: vypnuté", "shortcut_updated": "Klávesová skratka aktualizovaná"},
    "sl": {"shortcut_label": "Bližnjica, da Anki ostane na vrhu", "shortcut_prefix": "Bližnjica:", "placeholder": "Pritisnite bližnjico na tipkovnici", "save": "Sprejmi", "cancel": "Prekliči", "defaults": "Obnovi privzete vrednosti", "on": "Vedno na vrhu: vklopljeno", "off": "Vedno na vrhu: izklopljeno", "shortcut_updated": "Bližnjica na tipkovnici posodobljena"},
    "hr": {"shortcut_label": "Prečac za držanje Ankija na vrhu", "shortcut_prefix": "Prečac:", "placeholder": "Pritisnite tipkovnički prečac", "save": "Prihvati", "cancel": "Odustani", "defaults": "Vrati zadane vrijednosti", "on": "Uvijek na vrhu: uključeno", "off": "Uvijek na vrhu: isključeno", "shortcut_updated": "Tipkovnički prečac ažuriran"},
    "sr": {"shortcut_label": "Пречица да Anki остане на врху", "shortcut_prefix": "Пречица:", "placeholder": "Притисните пречицу на тастатури", "save": "Прихвати", "cancel": "Откажи", "defaults": "Врати подразумеване вредности", "on": "Увек на врху: укључено", "off": "Увек на врху: искључено", "shortcut_updated": "Пречица на тастатури ажурирана"},
    "bg": {"shortcut_label": "Клавишна комбинация, за да остане Anki отгоре", "shortcut_prefix": "Клавишна комбинация:", "placeholder": "Натиснете клавишната комбинация", "save": "Приеми", "cancel": "Отказ", "defaults": "Възстанови стойностите по подразбиране", "on": "Винаги отгоре: включено", "off": "Винаги отгоре: изключено", "shortcut_updated": "Клавишната комбинация е обновена"},
    "sv": {"shortcut_label": "Kortkommando för att hålla Anki överst", "shortcut_prefix": "Kortkommando:", "placeholder": "Tryck på kortkommandot", "save": "Acceptera", "cancel": "Avbryt", "defaults": "Återställ standardvärden", "on": "Alltid överst: på", "off": "Alltid överst: av", "shortcut_updated": "Kortkommando uppdaterat"},
    "da": {"shortcut_label": "Genvej til at holde Anki øverst", "shortcut_prefix": "Genvej:", "placeholder": "Tryk på genvejstasten", "save": "Accepter", "cancel": "Annuller", "defaults": "Gendan standardværdier", "on": "Altid øverst: til", "off": "Altid øverst: fra", "shortcut_updated": "Genvejstast opdateret"},
    "nb": {"shortcut_label": "Hurtigtast for å holde Anki øverst", "shortcut_prefix": "Hurtigtast:", "placeholder": "Trykk på hurtigtasten", "save": "Godta", "cancel": "Avbryt", "defaults": "Gjenopprett standardverdier", "on": "Alltid øverst: på", "off": "Alltid øverst: av", "shortcut_updated": "Hurtigtast oppdatert"},
    "fi": {"shortcut_label": "Pikanäppäin, joka pitää Ankin päällimmäisenä", "shortcut_prefix": "Pikanäppäin:", "placeholder": "Paina pikanäppäintä", "save": "Hyväksy", "cancel": "Peruuta", "defaults": "Palauta oletusarvot", "on": "Aina päällimmäisenä: käytössä", "off": "Aina päällimmäisenä: pois käytöstä", "shortcut_updated": "Pikanäppäin päivitetty"},
    "et": {"shortcut_label": "Kiirklahv, et hoida Anki pealmisena", "shortcut_prefix": "Kiirklahv:", "placeholder": "Vajutage kiirklahvi", "save": "Nõustu", "cancel": "Tühista", "defaults": "Taasta vaikeväärtused", "on": "Alati pealmine: sees", "off": "Alati pealmine: väljas", "shortcut_updated": "Kiirklahv uuendatud"},
    "lt": {"shortcut_label": "Spartusis klavišas, kad Anki liktų viršuje", "shortcut_prefix": "Spartusis klavišas:", "placeholder": "Paspauskite spartųjį klavišą", "save": "Priimti", "cancel": "Atšaukti", "defaults": "Atkurti numatytąsias reikšmes", "on": "Visada viršuje: įjungta", "off": "Visada viršuje: išjungta", "shortcut_updated": "Spartusis klavišas atnaujintas"},
    "lv": {"shortcut_label": "Īsinājumtaustiņš, lai Anki paliktu virspusē", "shortcut_prefix": "Īsinājumtaustiņš:", "placeholder": "Nospiediet īsinājumtaustiņu", "save": "Pieņemt", "cancel": "Atcelt", "defaults": "Atjaunot noklusējuma vērtības", "on": "Vienmēr virspusē: ieslēgts", "off": "Vienmēr virspusē: izslēgts", "shortcut_updated": "Īsinājumtaustiņš atjaunināts"},
    "hu": {"shortcut_label": "Billentyűparancs, hogy az Anki felül maradjon", "shortcut_prefix": "Billentyűparancs:", "placeholder": "Nyomja meg a billentyűparancsot", "save": "Elfogadás", "cancel": "Mégse", "defaults": "Alapértelmezett értékek visszaállítása", "on": "Mindig felül: bekapcsolva", "off": "Mindig felül: kikapcsolva", "shortcut_updated": "Billentyűparancs frissítve"},
    "el": {"shortcut_label": "Συντόμευση για να μένει το Anki σε πρώτο πλάνο", "shortcut_prefix": "Συντόμευση:", "placeholder": "Πατήστε τη συντόμευση πληκτρολογίου", "save": "Αποδοχή", "cancel": "Ακύρωση", "defaults": "Επαναφορά προεπιλογών", "on": "Πάντα σε πρώτο πλάνο: ενεργό", "off": "Πάντα σε πρώτο πλάνο: ανενεργό", "shortcut_updated": "Η συντόμευση πληκτρολογίου ενημερώθηκε"},
    "tr": {
        "shortcut_label": "Anki'yi üstte tutmak için kısayol",
        "shortcut_prefix": "Kısayol:",
        "placeholder": "Klavye kısayoluna basın",
        "save": "Kabul Et",
        "cancel": "İptal",
        "defaults": "Varsayılan değerleri geri yükle",
        "on": "Her zaman üstte: açık",
        "off": "Her zaman üstte: kapalı",
        "shortcut_updated": "Klavye kısayolu güncellendi",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Ko-fi",
        "kofi_tooltip": "Ko-fi'de AnkiCraft'ı destekle",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d Bu eklentiyi oyla",
        "report_button": "Hata bildir",
        "welcome_close": "Kapat",
        "welcome_body": (
            "Always on Top, Kart Ekle penceresini diğer tüm pencerelerin üzerine sabitler "
            "— Anki'ye geri dönmeden not eklemeye devam edebilirsiniz.\n\n"
            "Açmak veya kapatmak için yapılandırılmış kısayola (varsayılan: Ctrl+Shift+T) basın. "
            "Araçlar → Eklentiler → {name} → Yapılandırma'dan istediğiniz zaman değiştirin."
        ),
        "welcome_support_note": (
            "Bu eklenti ücretsiz ve açık kaynaklıdır (AGPLv3). "
            "Zaman kazandırıyorsa geliştirmeyi desteklemeyi düşünün!"
        ),
    },
    "ar": {
        "shortcut_label": "اختصار لإبقاء Anki في المقدمة",
        "shortcut_prefix": "الاختصار:",
        "placeholder": "اضغط اختصار لوحة المفاتيح",
        "save": "قبول",
        "cancel": "إلغاء",
        "defaults": "استعادة القيم الافتراضية",
        "on": "البقاء في المقدمة: مفعّل",
        "off": "البقاء في المقدمة: معطّل",
        "shortcut_updated": "تم تحديث اختصار لوحة المفاتيح",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Ko-fi",
        "kofi_tooltip": "ادعم AnkiCraft على Ko-fi",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d قيّم هذه الإضافة",
        "report_button": "الإبلاغ عن خطأ",
        "welcome_close": "إغلاق",
        "welcome_body": (
            "Always on Top يثبّت نافذة إضافة البطاقات فوق جميع النوافذ الأخرى "
            "— حتى تتمكن من الاستمرار في إضافة الملاحظات دون العودة إلى Anki.\n\n"
            "اضغط على الاختصار المُهيَّأ (الافتراضي: Ctrl+Shift+T) لتشغيله أو إيقافه. "
            "غيّره في أي وقت عبر الأدوات → الإضافات → {name} → الإعداد."
        ),
        "welcome_support_note": (
            "هذه الإضافة مجانية ومفتوحة المصدر (AGPLv3). "
            "إذا وفّرت لك وقتاً، فكّر في دعم تطويرها!"
        ),
    },
    "he": {
        "shortcut_label": "קיצור דרך להשארת Anki למעלה",
        "shortcut_prefix": "קיצור דרך:",
        "placeholder": "הקש על קיצור המקלדת",
        "save": "אישור",
        "cancel": "ביטול",
        "defaults": "שחזור ברירות המחדל",
        "on": "תמיד למעלה: פעיל",
        "off": "תמיד למעלה: כבוי",
        "shortcut_updated": "קיצור המקלדת עודכן",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Ko-fi",
        "kofi_tooltip": "תמוך ב-AnkiCraft ב-Ko-fi",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d דרג את התוסף",
        "report_button": "דיווח על באג",
        "welcome_close": "סגור",
        "welcome_body": (
            "Always on Top מצמיד את חלון הוספת הקלפים מעל כל החלונות האחרים "
            "— כדי שתוכל להמשיך להוסיף פתקים מבלי לחזור ל-Anki.\n\n"
            "לחץ על קיצור הדרך שהגדרת (ברירת מחדל: Ctrl+Shift+T) להפעלה/כיבוי. "
            "שנה אותו בכל עת דרך כלים → תוספות → {name} → הגדרות."
        ),
        "welcome_support_note": (
            "התוסף הזה חינמי ובקוד פתוח (AGPLv3). "
            "אם הוא חוסך לך זמן, שקול לתמוך בפיתוחו!"
        ),
    },
    "fa": {"shortcut_label": "میانبر برای نگه داشتن Anki در بالا", "shortcut_prefix": "میانبر:", "placeholder": "میانبر صفحه‌کلید را فشار دهید", "save": "تأیید", "cancel": "لغو", "defaults": "بازگرداندن مقادیر پیش‌فرض", "on": "همیشه در بالا: فعال", "off": "همیشه در بالا: غیرفعال", "shortcut_updated": "میانبر صفحه‌کلید به‌روزرسانی شد"},
    "hi": {"shortcut_label": "Anki को ऊपर रखने के लिए शॉर्टकट", "shortcut_prefix": "शॉर्टकट:", "placeholder": "कीबोर्ड शॉर्टकट दबाएँ", "save": "स्वीकार करें", "cancel": "रद्द करें", "defaults": "डिफ़ॉल्ट मान पुनर्स्थापित करें", "on": "हमेशा ऊपर: चालू", "off": "हमेशा ऊपर: बंद", "shortcut_updated": "कीबोर्ड शॉर्टकट अपडेट किया गया"},
    "th": {"shortcut_label": "ปุ่มลัดเพื่อให้ Anki อยู่บนสุด", "shortcut_prefix": "ปุ่มลัด:", "placeholder": "กดปุ่มลัดบนแป้นพิมพ์", "save": "ยอมรับ", "cancel": "ยกเลิก", "defaults": "คืนค่าเริ่มต้น", "on": "ปักหมุดอยู่บนสุด: เปิด", "off": "ปักหมุดอยู่บนสุด: ปิด", "shortcut_updated": "อัปเดตปุ่มลัดแล้ว"},
    "vi": {"shortcut_label": "Phím tắt để giữ Anki ở trên cùng", "shortcut_prefix": "Phím tắt:", "placeholder": "Nhấn phím tắt", "save": "Chấp nhận", "cancel": "Hủy", "defaults": "Khôi phục giá trị mặc định", "on": "Luôn ở trên cùng: bật", "off": "Luôn ở trên cùng: tắt", "shortcut_updated": "Đã cập nhật phím tắt"},
    "id": {"shortcut_label": "Pintasan untuk menjaga Anki tetap di atas", "shortcut_prefix": "Pintasan:", "placeholder": "Tekan pintasan papan ketik", "save": "Terima", "cancel": "Batal", "defaults": "Pulihkan nilai bawaan", "on": "Selalu di atas: aktif", "off": "Selalu di atas: nonaktif", "shortcut_updated": "Pintasan papan ketik diperbarui"},
    "ms": {"shortcut_label": "Pintasan untuk mengekalkan Anki di atas", "shortcut_prefix": "Pintasan:", "placeholder": "Tekan pintasan papan kekunci", "save": "Terima", "cancel": "Batal", "defaults": "Pulihkan nilai lalai", "on": "Sentiasa di atas: dihidupkan", "off": "Sentiasa di atas: dimatikan", "shortcut_updated": "Pintasan papan kekunci dikemas kini"},
    "ja": {
        "shortcut_label": "Ankiを最前面に保つショートカット",
        "shortcut_prefix": "ショートカット:",
        "placeholder": "キーボードショートカットを押してください",
        "save": "OK",
        "cancel": "キャンセル",
        "defaults": "既定値に戻す",
        "on": "常に最前面: 有効",
        "off": "常に最前面: 無効",
        "shortcut_updated": "キーボードショートカットを更新しました",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Ko-fi",
        "kofi_tooltip": "Ko-fiでAnkiCraftを応援",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d このアドオンを評価",
        "report_button": "バグを報告",
        "welcome_close": "閉じる",
        "welcome_body": (
            "Always on Topはカード追加ウィンドウをすべてのウィンドウの最前面に固定します "
            "— Ankiに戻ることなくノートを追加し続けることができます。\n\n"
            "設定済みショートカット（デフォルト：Ctrl+Shift+T）を押してオン/オフを切り替えてください。"
            "ツール → アドオン → {name} → 設定からいつでも変更できます。"
        ),
        "welcome_support_note": (
            "このアドオンは無料かつオープンソース（AGPLv3）です。"
            "時間を節約できた場合は、開発サポートをご検討ください！"
        ),
    },
    "ko": {
        "shortcut_label": "Anki를 항상 위에 유지하는 단축키",
        "shortcut_prefix": "단축키:",
        "placeholder": "단축키를 누르세요",
        "save": "확인",
        "cancel": "취소",
        "defaults": "기본값 복원",
        "on": "항상 위에 표시: 켜짐",
        "off": "항상 위에 표시: 꺼짐",
        "shortcut_updated": "단축키가 업데이트되었습니다",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Ko-fi",
        "kofi_tooltip": "Ko-fi에서 AnkiCraft 후원하기",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d 이 애드온 평가하기",
        "report_button": "버그 신고",
        "welcome_close": "닫기",
        "welcome_body": (
            "Always on Top은 카드 추가 창을 모든 창 위에 고정합니다 "
            "— Anki로 돌아가지 않고도 노트를 계속 추가할 수 있습니다.\n\n"
            "설정된 단축키(기본: Ctrl+Shift+T)를 눌러 켜거나 끄세요. "
            "도구 → 애드온 → {name} → 설정에서 언제든지 변경할 수 있습니다."
        ),
        "welcome_support_note": (
            "이 애드온은 무료이며 오픈 소스(AGPLv3)입니다. "
            "시간을 절약했다면 개발을 지원해 주세요!"
        ),
    },
    "zh_CN": {
        "shortcut_label": "保持 Anki 置顶的快捷键",
        "shortcut_prefix": "快捷键：",
        "placeholder": "请按下快捷键",
        "save": "确定",
        "cancel": "取消",
        "defaults": "恢复默认值",
        "on": "始终置顶：已开启",
        "off": "始终置顶：已关闭",
        "shortcut_updated": "快捷键已更新",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Ko-fi",
        "kofi_tooltip": "在Ko-fi上支持AnkiCraft",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d 评价此插件",
        "report_button": "报告错误",
        "welcome_close": "关闭",
        "welcome_body": (
            "Always on Top 将添加卡片窗口固定在所有其他窗口上方 "
            "— 让您可以持续添加笔记，无需切换回 Anki。\n\n"
            "按已配置的快捷键（默认：Ctrl+Shift+T）开启或关闭。"
            "可随时通过 工具 → 插件 → {name} → 配置 进行更改。"
        ),
        "welcome_support_note": (
            "此插件免费且开源（AGPLv3）。"
            "如果节省了您的时间，欢迎支持其开发！"
        ),
    },
    "zh_TW": {
        "shortcut_label": "保持 Anki 置頂的快捷鍵",
        "shortcut_prefix": "快捷鍵：",
        "placeholder": "請按下快捷鍵",
        "save": "確定",
        "cancel": "取消",
        "defaults": "還原預設值",
        "on": "永遠置頂：已開啟",
        "off": "永遠置頂：已關閉",
        "shortcut_updated": "快捷鍵已更新",
        # Marketing keys
        "version_line": "{name} v{version}",
        "welcome_title": "{name} v{version}",
        "kofi_button": "☕ Ko-fi",
        "kofi_tooltip": "在Ko-fi上支持AnkiCraft",
        "patreon_button": "♥ Patreon",
        "rate_button": "\U0001f44d 評價此插件",
        "report_button": "回報錯誤",
        "welcome_close": "關閉",
        "welcome_body": (
            "Always on Top 將新增卡片視窗固定在所有其他視窗上方 "
            "— 讓您可以持續新增筆記，無需切換回 Anki。\n\n"
            "按已設定的快捷鍵（預設：Ctrl+Shift+T）開啟或關閉。"
            "可隨時透過 工具 → 插件 → {name} → 設定 進行更改。"
        ),
        "welcome_support_note": (
            "此插件免費且開源（AGPLv3）。"
            "如果節省了您的時間，歡迎支持其開發！"
        ),
    },
    "eo": {"shortcut_label": "Klavkombino por teni Anki supre", "shortcut_prefix": "Klavkombino:", "placeholder": "Premu la klavkombinon", "save": "Akcepti", "cancel": "Nuligi", "defaults": "Restarigi defaŭltajn valorojn", "on": "Ĉiam supre: ŝaltita", "off": "Ĉiam supre: malŝaltita", "shortcut_updated": "Klavkombino ĝisdatigita"},
    "af": {"shortcut_label": "Kortpad om Anki bo-op te hou", "shortcut_prefix": "Kortpad:", "placeholder": "Druk die sleutelbordkortpad", "save": "Aanvaar", "cancel": "Kanselleer", "defaults": "Herstel verstekwaardes", "on": "Altyd bo-op: aan", "off": "Altyd bo-op: af", "shortcut_updated": "Sleutelbordkortpad opgedateer"},
    "be": {"shortcut_label": "Спалучэнне клавіш, каб трымаць Anki зверху", "shortcut_prefix": "Спалучэнне клавіш:", "placeholder": "Націсніце спалучэнне клавіш", "save": "Прыняць", "cancel": "Адмяніць", "defaults": "Аднавіць прадвызначаныя значэнні", "on": "Заўсёды зверху: уключана", "off": "Заўсёды зверху: выключана", "shortcut_updated": "Спалучэнне клавіш абноўлена"},
    "eu": {"shortcut_label": "Anki gainean mantentzeko lasterbidea", "shortcut_prefix": "Lasterbidea:", "placeholder": "Sakatu teklatu-lasterbidea", "save": "Onartu", "cancel": "Utzi", "defaults": "Leheneratu balio lehenetsiak", "on": "Beti gainean: aktibatuta", "off": "Beti gainean: desaktibatuta", "shortcut_updated": "Teklatu-lasterbidea eguneratuta"},
    "ga": {"shortcut_label": "Aicearra chun Anki a choinneáil ar barr", "shortcut_prefix": "Aicearra:", "placeholder": "Brúigh an t-aicearra méarchláir", "save": "Glac leis", "cancel": "Cealaigh", "defaults": "Athchóirigh na réamhshocruithe", "on": "I gcónaí ar bharr: ar siúl", "off": "I gcónaí ar bharr: as", "shortcut_updated": "Aicearra méarchláir nuashonraithe"},
    "hy": {"shortcut_label": "Դյուրանցում՝ Anki-ն վերևում պահելու համար", "shortcut_prefix": "Դյուրանցում.", "placeholder": "Սեղմեք ստեղնաշարի դյուրանցումը", "save": "Ընդունել", "cancel": "Չեղարկել", "defaults": "Վերականգնել լռելյայն արժեքները", "on": "Միշտ վերևում. միացված", "off": "Միշտ վերևում. անջատված", "shortcut_updated": "Ստեղնաշարի դյուրանցումը թարմացվել է"},
    "jbo": {"shortcut_label": "lerpinsle lo nu Anki gapru", "shortcut_prefix": "lerpinsle:", "placeholder": "ko danre lo lerpinsle", "save": "cpacu", "cancel": "sisti", "defaults": "xruti fi le krasi", "on": "ca'o gapru: cnino", "off": "ca'o gapru: nalcnino", "shortcut_updated": "lerpinsle basti"},
    "la": {"shortcut_label": "Compendium ut Anki supra maneat", "shortcut_prefix": "Compendium:", "placeholder": "Preme compendium claviaturae", "save": "Accipe", "cancel": "Cancella", "defaults": "Valores primos restituere", "on": "Semper supra: activum", "off": "Semper supra: inactivum", "shortcut_updated": "Compendium claviaturae renovatum"},
    "mn": {"shortcut_label": "Anki-г дээр байлгах товчлол", "shortcut_prefix": "Товчлол:", "placeholder": "Товчлолыг дарна уу", "save": "Зөвшөөрөх", "cancel": "Цуцлах", "defaults": "Анхны утгыг сэргээх", "on": "Үргэлж дээр: асаалттай", "off": "Үргэлж дээр: унтраалттай", "shortcut_updated": "Товчлол шинэчлэгдлээ"},
    "my": {"shortcut_label": "Anki ကို အပေါ်တွင် ထားရန် ဖြတ်လမ်း", "shortcut_prefix": "ဖြတ်လမ်း:", "placeholder": "ကီးဘုတ်ဖြတ်လမ်းကို နှိပ်ပါ", "save": "လက်ခံပါ", "cancel": "မလုပ်တော့ပါ", "defaults": "မူလတန်ဖိုးများ ပြန်လည်ရယူပါ", "on": "အမြဲအပေါ်တွင်: ဖွင့်ထားသည်", "off": "အမြဲအပေါ်တွင်: ပိတ်ထားသည်", "shortcut_updated": "ကီးဘုတ်ဖြတ်လမ်း အပ်ဒိတ်လုပ်ပြီးပါပြီ"},
    "oc": {"shortcut_label": "Acorchi per gardar Anki amont", "shortcut_prefix": "Acorchi :", "placeholder": "Quichatz l'acorchi de clavièr", "save": "Acceptar", "cancel": "Anullar", "defaults": "Restablir las valors per defaut", "on": "Totjorn amont : activat", "off": "Totjorn amont : desactivat", "shortcut_updated": "Acorchi de clavièr actualizat"},
    "sq": {"shortcut_label": "Shkurtore për ta mbajtur Anki-n sipër", "shortcut_prefix": "Shkurtore:", "placeholder": "Shtypni shkurtoren e tastierës", "save": "Prano", "cancel": "Anulo", "defaults": "Rikthe vlerat e parazgjedhura", "on": "Gjithmonë sipër: aktivizuar", "off": "Gjithmonë sipër: çaktivizuar", "shortcut_updated": "Shkurtorja e tastierës u përditësua"},
    "ug": {"shortcut_label": "Anki نى ئۈستىدە تۇتۇش تېزلەتمىسى", "shortcut_prefix": "تېزلەتمە:", "placeholder": "كۇنۇپكا تېزلەتمىسىنى بېسىڭ", "save": "قوبۇل قىلىش", "cancel": "ۋاز كەچمەك", "defaults": "كۆڭۈلدىكى قىممەتلەرنى ئەسلىگە كەلتۈرۈش", "on": "ھەمىشە ئۈستىدە: ئوچۇق", "off": "ھەمىشە ئۈستىدە: تاقاق", "shortcut_updated": "كۇنۇپكا تېزلەتمىسى يېڭىلاندى"},
    "uz": {"shortcut_label": "Anki-ni tepada ushlab turish uchun yorliq", "shortcut_prefix": "Yorliq:", "placeholder": "Klaviatura yorlig'ini bosing", "save": "Qabul qilish", "cancel": "Bekor qilish", "defaults": "Standart qiymatlarni tiklash", "on": "Doim tepada: yoqilgan", "off": "Doim tepada: o'chirilgan", "shortcut_updated": "Klaviatura yorlig'i yangilandi"},
    "fil": {"shortcut_label": "Shortcut para panatilihing nasa ibabaw ang Anki", "shortcut_prefix": "Shortcut:", "placeholder": "Pindutin ang keyboard shortcut", "save": "Tanggapin", "cancel": "Kanselahin", "defaults": "Ibalik ang mga default na halaga", "on": "Laging nasa ibabaw: naka-on", "off": "Laging nasa ibabaw: naka-off", "shortcut_updated": "Na-update ang shortcut sa keyboard"},
}


def _resolve(code: str) -> str:
    code = code.replace("-", "_")
    parts = code.split("_")
    primary = parts[0].lower()
    region = parts[1].upper() if len(parts) > 1 else ""
    if primary == "zh":
        return "zh_TW" if region in ("TW", "HK", "MO") or "HANT" in code.upper() else "zh_CN"
    if primary == "pt":
        return "pt_PT" if region == "PT" else "pt_BR"
    if primary in ("fil", "tl"):
        return "fil"
    return primary if primary in TRANSLATIONS else FALLBACK


@lru_cache(maxsize=1)
def current_lang() -> str:
    try:
        import anki.lang

        raw = (
            getattr(anki.lang, "current_lang", None)
            or getattr(anki.lang, "currentLang", None)
            or ""
        )
        code = raw if isinstance(raw, str) else ""
        return _resolve(code)
    except Exception as exc:
        print(f"[always_on_top] strings.current_lang: {exc!r}")
        return FALLBACK


def tr(key: str, **values: str) -> str:
    table = TRANSLATIONS.get(current_lang(), TRANSLATIONS[FALLBACK])
    value = table.get(key)
    if value is None:
        value = TRANSLATIONS[FALLBACK].get(key, key)
    if not values:
        return value
    try:
        return value.format(**values)
    except (KeyError, IndexError):
        return value
