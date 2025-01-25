import typing as t
from dataclasses import dataclass, field

UnauthorisedPageBehaviour = t.Literal["lock", "hide"]


@dataclass(frozen=True)
class UserGroup:
    name_: str  # needs the trailing `_` to be compatible for us in an Enum
    uuid: str


@dataclass
class Page:
    name: str
    render_func_entrypoint: str


@dataclass
class MenuPage(Page):
    icon: str
    authorised_user_groups: list[UserGroup] = field(default_factory=lambda: [])
    unauthorised_behaviour: UnauthorisedPageBehaviour = "lock"


class MenuPages(list[MenuPage]):
    """A list of `MenuPage`s"""


@dataclass
class StreamlitPageConfig:
    app_title: str
    app_icon: str
    app_subtitle: str
    layout: t.Literal["centered", "wide"] = "wide"


@dataclass
class AppConfig:
    streamlit_page_config: StreamlitPageConfig
    menu_pages: MenuPages
