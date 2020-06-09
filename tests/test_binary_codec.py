from kintercrypt.binary_codec import binary_string, string_binary


def test_both():
    assert binary_string(*string_binary('Hello World')) == 'Hello World'
    assert binary_string(*string_binary('123ę')) == '123ę'
    assert binary_string(*string_binary(' ')) == ' '

    # The following examples are from https://stackoverflow.com/a/51539774/10763533
    # Emoji
    assert binary_string(*string_binary('👱👱🏻👱🏼👱🏽👱🏾👱🏿')) == '👱👱🏻👱🏼👱🏽👱🏾👱🏿'
    assert binary_string(*string_binary('🧟‍♀️🧟‍♂️')) == '🧟‍♀️🧟‍♂️'
    assert binary_string(*string_binary('👨‍❤️‍💋‍👨👩‍👩‍👧‍👦️')) == '👨‍❤️‍💋‍👨👩‍👩‍👧‍👦️'

    # Words in different directions
    assert binary_string(*string_binary('اختبار النص')) == 'اختبار النص'
    assert binary_string(*string_binary('اليسار')) == 'اليسار'

