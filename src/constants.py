from types import SimpleNamespace

import emoji

from src.utils.keyboard import create_keyboard

keys = SimpleNamespace(
    settings=emoji.emojize(':gear: Setting'),
    exit=emoji.emojize(':cross_mark: Exit'),
)

keyboards= SimpleNamespace(
    main=create_keyboard(keys.exit,keys.settings),
)
