from ezconfig import EzConfig, KeyPrompt

ez = EzConfig(
    KeyPrompt("DELAY", default_value=5, value_type=float),
    KeyPrompt("LINK", can_be_empty=False),
    KeyPrompt("USE_PROXY", value_type=bool, can_be_empty=False),
    KeyPrompt("USE_CACHE", value_type=bool, can_be_empty=False),
)
ez.configure()

print(f"Your link: ", ez.config["LINK"])