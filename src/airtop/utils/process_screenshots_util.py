import re
import base64
from typing import List, Optional, Tuple
from airtop import types

class ProcessScreenshotsResponse:
    def __init__(self, index: int, success: bool, mime_type: Optional[str] = None, binary_data: Optional[bytes] = None, error: Optional[Exception] = None):
        self.index = index
        self.success = success
        self.mime_type = mime_type
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
            mime_type, base64_data = extract_mime_and_base64(screenshot.data_url)
            binary_data = base64.b64decode(base64_data)
            processed_screenshots.append(ProcessScreenshotsResponse(index, True, binary_data=binary_data, mime_type=mime_type))
        except Exception as err:
            print(f"Error processing screenshot {index}:", err)
            processed_screenshots.append(ProcessScreenshotsResponse(index, False, error=err))

    return processed_screenshots

def extract_mime_and_base64(data_url: str) -> Tuple[str, str]:
    """Extracts MIME type and Base64 data from a data URL, defaults to image/jpeg."""
    match = re.match(r"data:(image/\w+);base64,(.+)", data_url)
    if match:
        return match.group(1), match.group(2)
    return "image/jpeg", data_url.replace("data:image/jpeg;base64,", "")
