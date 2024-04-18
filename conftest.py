from typing import Any, Generator

from playwright.sync_api import  sync_playwright, Playwright
from pytest import  fixture

@fixture(scope='function')
def playwright_fixture() -> Generator[Playwright, Any, None]:
    with sync_playwright() as playwright:
        yield playwright
