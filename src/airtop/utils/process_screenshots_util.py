from typing import List, Optional
import base64
from airtop import types

class ProcessScreenshotsResponse:
    def __init__(self, index: int, success: bool, binary_data: Optional[bytes] = None, error: Optional[Exception] = None):
        self.index = index
        self.success = success
        self.binary_data = binary_data
        self.error = error

def process_screenshots(response: types.AiPromptResponse) -> List[ProcessScreenshotsResponse]:
    screenshots = response.meta.screenshots

    if not screenshots:
        return []

    processed_screenshots = []
    for index, screenshot in enumerate(screenshots):
        if not screenshot.data_url:
            processed_screenshots.append(ProcessScreenshotsResponse(index, False, error=Exception("Screenshot data URL not found")))
            continue

        try:
            base64_data = screenshot.data_url.replace('data:image/jpeg;base64,', '')
            binary_data = base64.b64decode(base64_data)
            processed_screenshots.append(ProcessScreenshotsResponse(index, True, binary_data=binary_data))
        except Exception as err:
            print(f"Error processing screenshot {index}:", err)
            processed_screenshots.append(ProcessScreenshotsResponse(index, False, error=err))

    return processed_screenshots
