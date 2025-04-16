# Reference
## Windows
<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">async_create_automation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create an automation of a browser window asynchronously
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.async_create_automation(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The session id for the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — The Airtop window id of the browser window.
    
</dd>
</dl>

<dl>
<dd>

**async_:** `typing.Optional[AsyncConfig]` — Async configuration options.
    
</dd>
</dl>

<dl>
<dd>

**client_request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[CreateAutomationRequestBodyConfiguration]` — Request configuration
    
</dd>
</dl>

<dl>
<dd>

**cost_threshold_credits:** `typing.Optional[int]` — A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).
    
</dd>
</dl>

<dl>
<dd>

**time_threshold_seconds:** `typing.Optional[int]` 

A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

This setting does not extend the maximum session duration provided at the time of session creation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">async_create_form_filler</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a form filler automation asynchronously
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.async_create_form_filler(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The session id for the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — The Airtop window id of the browser window.
    
</dd>
</dl>

<dl>
<dd>

**async_:** `typing.Optional[AsyncConfig]` — Async configuration options.
    
</dd>
</dl>

<dl>
<dd>

**client_request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[CreateAutomationRequestBodyConfiguration]` — Request configuration
    
</dd>
</dl>

<dl>
<dd>

**cost_threshold_credits:** `typing.Optional[int]` — A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).
    
</dd>
</dl>

<dl>
<dd>

**time_threshold_seconds:** `typing.Optional[int]` 

A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

This setting does not extend the maximum session duration provided at the time of session creation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">async_execute_automation</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute an automation of a browser window asynchronously
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.async_execute_automation(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
    automation_id="automationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The session id for the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — The Airtop window id of the browser window.
    
</dd>
</dl>

<dl>
<dd>

**automation_id:** `str` — The ID of the automation to execute
    
</dd>
</dl>

<dl>
<dd>

**async_:** `typing.Optional[AsyncConfig]` — Async configuration options.
    
</dd>
</dl>

<dl>
<dd>

**client_request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cost_threshold_credits:** `typing.Optional[int]` — A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Optional parameters to pass to the automation execution
    
</dd>
</dl>

<dl>
<dd>

**time_threshold_seconds:** `typing.Optional[int]` 

A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

This setting does not extend the maximum session duration provided at the time of session creation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">async_fill_form</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fill a form of a browser window asynchronously using a form-filler automation
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.async_fill_form(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
    automation_id="automationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The session id for the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — The Airtop window id of the browser window.
    
</dd>
</dl>

<dl>
<dd>

**automation_id:** `str` — The ID of the automation to execute
    
</dd>
</dl>

<dl>
<dd>

**async_:** `typing.Optional[AsyncConfig]` — Async configuration options.
    
</dd>
</dl>

<dl>
<dd>

**client_request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cost_threshold_credits:** `typing.Optional[int]` — A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Optional parameters to pass to the automation execution
    
</dd>
</dl>

<dl>
<dd>

**time_threshold_seconds:** `typing.Optional[int]` 

A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

This setting does not extend the maximum session duration provided at the time of session creation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Creates a new browser window in a session. Optionally, you can specify a url to load on the window upon creation.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.create(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — ID of the session that owns the window.
    
</dd>
</dl>

<dl>
<dd>

**screen_resolution:** `typing.Optional[str]` — Affects the live view configuration. By default, a live view will fill the parent frame (or local window if loaded directly) when initially loaded, causing the browser window to be resized to match. This parameter can be used to instead configure the returned liveViewUrl so that the live view is loaded with fixed dimensions (e.g. 1280x720), resizing the browser window to match, and then disallows any further resizing from the live view.
    
</dd>
</dl>

<dl>
<dd>

**url:** `typing.Optional[str]` — Initial url to navigate to
    
</dd>
</dl>

<dl>
<dd>

**wait_until:** `typing.Optional[CreateWindowInputV1BodyWaitUntil]` — Wait until the specified loading event occurs. Defaults to 'load', which waits until the page dom and it's assets have loaded. 'domContentLoaded' will wait until the dom has loaded, 'complete' will wait until the page and all it's iframes have loaded it's dom and assets. 'noWait' will not wait for any loading event and will return immediately.
    
</dd>
</dl>

<dl>
<dd>

**wait_until_timeout_seconds:** `typing.Optional[int]` — Maximum time in seconds to wait for the specified loading event to occur before timing out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">get_window_info</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get information about a browser window in a session, including the live view url.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.get_window_info(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="7334da2a-91b0-42c5-6156-76a5eba87430",
    screen_resolution="1280x720",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — ID of the session that owns the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — ID of the browser window, which can either be a normal AirTop windowId or a [CDP TargetId](https://chromedevtools.github.io/devtools-protocol/tot/Target/#type-TargetID) from a browser automation library like Puppeteer (typically associated with the page or main frame). Our SDKs will handle retrieving a TargetId for you from various popular browser automation libraries, but we also have details in our guides on how to do it manually.
    
</dd>
</dl>

<dl>
<dd>

**include_navigation_bar:** `typing.Optional[bool]` — Affects the live view configuration. A navigation bar is not shown in the live view of a browser by default. Set this to true to configure the returned liveViewUrl so that a navigation bar is rendered, allowing users to easily navigate the browser to other pages from the live view.
    
</dd>
</dl>

<dl>
<dd>

**disable_resize:** `typing.Optional[bool]` — Affects the live view configuration. Set to true to configure the returned liveViewUrl so that the ability to resize the browser window from the live view is disabled (resizing is allowed by default). Note that, at initial load, the live view will automatically fill the parent frame (or local window if loaded directly) and cause the browser window to be resized to match. This parameter does not affect that initial load behavior. See screenResolution for a way to set a fixed size for the live view.
    
</dd>
</dl>

<dl>
<dd>

**screen_resolution:** `typing.Optional[str]` — Affects the live view configuration. By default, a live view will fill the parent frame (or local window if loaded directly) when initially loaded, causing the browser window to be resized to match. This parameter can be used to instead configure the returned liveViewUrl so that the live view is loaded with fixed dimensions (e.g. 1280x720), resizing the browser window to match, and then disallows any further resizing from the live view.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">load_url</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Loads a specified url on a given window
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.load_url(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="7334da2a-91b0-42c5-6156-76a5eba87430",
    url="https://www.airtop.ai",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — ID of the session that owns the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — Airtop window ID of the browser window.
    
</dd>
</dl>

<dl>
<dd>

**url:** `str` — Url to navigate to
    
</dd>
</dl>

<dl>
<dd>

**wait_until:** `typing.Optional[WindowLoadUrlV1BodyWaitUntil]` — Wait until the specified loading event occurs. Defaults to 'load', which waits until the page dom and it's assets have loaded. 'domContentLoaded' will wait until the dom has loaded, 'complete' will wait until the page and all it's iframes have loaded it's dom and assets. 'noWait' will not wait for any loading event and will return immediately.
    
</dd>
</dl>

<dl>
<dd>

**wait_until_timeout_seconds:** `typing.Optional[int]` — Maximum time in seconds to wait for the specified loading event to occur before timing out.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">close</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Closes a browser window in a session
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.close(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="7334da2a-91b0-42c5-6156-76a5eba87430",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — ID of the session that owns the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — Airtop window ID of the browser window.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">click</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a click interaction in a specific browser window
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.click(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
    element_description="The login button",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The session id for the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — The Airtop window id of the browser window.
    
</dd>
</dl>

<dl>
<dd>

**element_description:** `str` — A natural language description of the element to click.
    
</dd>
</dl>

<dl>
<dd>

**client_request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[ClickConfig]` — Request configuration
    
</dd>
</dl>

<dl>
<dd>

**cost_threshold_credits:** `typing.Optional[int]` — A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).
    
</dd>
</dl>

<dl>
<dd>

**time_threshold_seconds:** `typing.Optional[int]` 

A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

This setting does not extend the maximum session duration provided at the time of session creation.
    
</dd>
</dl>

<dl>
<dd>

**wait_for_navigation:** `typing.Optional[bool]` — If true, Airtop AI will wait for the navigation to complete after clicking the element.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">create_form_filler</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Create a form-filler automation synchronously for the form loaded in the browser window
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.create_form_filler(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The session id for the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — The Airtop window id of the browser window.
    
</dd>
</dl>

<dl>
<dd>

**async_:** `typing.Optional[AsyncConfig]` — Async configuration options.
    
</dd>
</dl>

<dl>
<dd>

**client_request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[CreateAutomationRequestBodyConfiguration]` — Request configuration
    
</dd>
</dl>

<dl>
<dd>

**cost_threshold_credits:** `typing.Optional[int]` — A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).
    
</dd>
</dl>

<dl>
<dd>

**time_threshold_seconds:** `typing.Optional[int]` 

A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

This setting does not extend the maximum session duration provided at the time of session creation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">fill_form</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Fill a form of a browser window synchronously using a form-filler automation
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.fill_form(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
    automation_id="automationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The session id for the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — The Airtop window id of the browser window.
    
</dd>
</dl>

<dl>
<dd>

**automation_id:** `str` — The ID of the automation to execute
    
</dd>
</dl>

<dl>
<dd>

**async_:** `typing.Optional[AsyncConfig]` — Async configuration options.
    
</dd>
</dl>

<dl>
<dd>

**client_request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cost_threshold_credits:** `typing.Optional[int]` — A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).
    
</dd>
</dl>

<dl>
<dd>

**parameters:** `typing.Optional[typing.Dict[str, typing.Optional[typing.Any]]]` — Optional parameters to pass to the automation execution
    
</dd>
</dl>

<dl>
<dd>

**time_threshold_seconds:** `typing.Optional[int]` 

A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

This setting does not extend the maximum session duration provided at the time of session creation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">hover</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a hover interaction in a specific browser window
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.hover(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
    element_description="The search box input in the top right corner",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The session id for the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — The Airtop window id of the browser window.
    
</dd>
</dl>

<dl>
<dd>

**element_description:** `str` — A natural language description of where to hover (e.g. 'the search box', 'username field'). The interaction will be aborted if the target element cannot be found.
    
</dd>
</dl>

<dl>
<dd>

**client_request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[MicroInteractionConfigWithExperimental]` — Request configuration
    
</dd>
</dl>

<dl>
<dd>

**cost_threshold_credits:** `typing.Optional[int]` — A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).
    
</dd>
</dl>

<dl>
<dd>

**time_threshold_seconds:** `typing.Optional[int]` 

A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

This setting does not extend the maximum session duration provided at the time of session creation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">monitor</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.monitor(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
    condition="Determine if the user appears to be signed in to the website",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The session id for the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — The Airtop window id of the browser window.
    
</dd>
</dl>

<dl>
<dd>

**condition:** `str` — A natural language description of the condition to monitor for in the browser window.
    
</dd>
</dl>

<dl>
<dd>

**client_request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[MonitorConfig]` — Monitor configuration. If not specified, defaults to an interval monitor with a 5 second interval.
    
</dd>
</dl>

<dl>
<dd>

**cost_threshold_credits:** `typing.Optional[int]` — A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).
    
</dd>
</dl>

<dl>
<dd>

**time_threshold_seconds:** `typing.Optional[int]` 

A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

This setting does not extend the maximum session duration provided at the time of session creation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">page_query</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit a prompt that queries the content of a specific browser window. You may extract content from the page, or ask a question about the page and allow the AI to answer it (ex. Is the user logged in?).
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.page_query(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
    prompt="What is the main idea of this page?",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The session id for the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — The Airtop window id of the browser window.
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `str` — The prompt to submit about the content in the browser window.
    
</dd>
</dl>

<dl>
<dd>

**client_request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[PageQueryConfig]` — Request configuration
    
</dd>
</dl>

<dl>
<dd>

**cost_threshold_credits:** `typing.Optional[int]` — A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).
    
</dd>
</dl>

<dl>
<dd>

**follow_pagination_links:** `typing.Optional[bool]` — Make a best effort attempt to load more content items than are originally displayed on the page, e.g. by following pagination links, clicking controls to load more content, utilizing infinite scrolling, etc. This can be quite a bit more costly, but may be necessary for sites that require additional interaction to show the needed results. You can provide constraints in your prompt (e.g. on the total number of pages or results to consider).
    
</dd>
</dl>

<dl>
<dd>

**time_threshold_seconds:** `typing.Optional[int]` 

A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

This setting does not extend the maximum session duration provided at the time of session creation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">paginated_extraction</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Submit a prompt that queries the content of a specific browser window and paginates through pages to return a list of results.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.paginated_extraction(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
    prompt="This site contains a list of results about <provide details about the list>. Navigate through 3 pages of results and return the title and <provide details about the data you want to extract> about each result in this list.",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The session id for the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — The Airtop window id of the browser window.
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `str` — A prompt providing the Airtop AI model with additional direction or constraints about the page and the details you want to extract from the page.
    
</dd>
</dl>

<dl>
<dd>

**client_request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[PaginatedExtractionConfig]` — Request configuration
    
</dd>
</dl>

<dl>
<dd>

**cost_threshold_credits:** `typing.Optional[int]` — A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).
    
</dd>
</dl>

<dl>
<dd>

**time_threshold_seconds:** `typing.Optional[int]` 

A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

This setting does not extend the maximum session duration provided at the time of session creation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">prompt_content</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is deprecated. Please use the `pageQuery` endpoint instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.prompt_content(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
    prompt="What is the main idea of this page?",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The session id for the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — The Airtop window id of the browser window.
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `str` — The prompt to submit about the content in the browser window.
    
</dd>
</dl>

<dl>
<dd>

**client_request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[PageQueryConfig]` — Request configuration
    
</dd>
</dl>

<dl>
<dd>

**cost_threshold_credits:** `typing.Optional[int]` — A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).
    
</dd>
</dl>

<dl>
<dd>

**follow_pagination_links:** `typing.Optional[bool]` — Make a best effort attempt to load more content items than are originally displayed on the page, e.g. by following pagination links, clicking controls to load more content, utilizing infinite scrolling, etc. This can be quite a bit more costly, but may be necessary for sites that require additional interaction to show the needed results. You can provide constraints in your prompt (e.g. on the total number of pages or results to consider).
    
</dd>
</dl>

<dl>
<dd>

**time_threshold_seconds:** `typing.Optional[int]` 

A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

This setting does not extend the maximum session duration provided at the time of session creation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">scrape_content</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Scrape a window and return the content as markdown
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.scrape_content(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The session id for the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — The Airtop window id of the browser window to scrape.
    
</dd>
</dl>

<dl>
<dd>

**client_request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**cost_threshold_credits:** `typing.Optional[int]` — A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).
    
</dd>
</dl>

<dl>
<dd>

**time_threshold_seconds:** `typing.Optional[int]` 

A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

This setting does not extend the maximum session duration provided at the time of session creation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">screenshot</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Take a screenshot of a browser window
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.screenshot(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The session id for the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — The Airtop window id of the browser window.
    
</dd>
</dl>

<dl>
<dd>

**client_request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[ScreenshotRequestConfig]` — Request configuration
    
</dd>
</dl>

<dl>
<dd>

**cost_threshold_credits:** `typing.Optional[int]` — A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).
    
</dd>
</dl>

<dl>
<dd>

**time_threshold_seconds:** `typing.Optional[int]` 

A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

This setting does not extend the maximum session duration provided at the time of session creation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">scroll</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a scroll interaction in a specific browser window
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.scroll(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The session id for the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — The Airtop window id of the browser window.
    
</dd>
</dl>

<dl>
<dd>

**client_request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[MicroInteractionConfig]` — Request configuration
    
</dd>
</dl>

<dl>
<dd>

**cost_threshold_credits:** `typing.Optional[int]` — A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).
    
</dd>
</dl>

<dl>
<dd>

**scroll_by:** `typing.Optional[ScrollByConfig]` — The amount of pixels/percentage to scroll horizontally or vertically relative to the current scroll position. Positive values scroll right and down, negative values scroll left and up. If a scrollToElement value is provided, scrollBy/scrollToEdge values will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**scroll_to_edge:** `typing.Optional[ScrollToEdgeConfig]` — Scroll to the top or bottom of the page, or to the left or right of the page. ScrollToEdge values will take precedence over the scrollBy values, and scrollToEdge will be executed first. If a scrollToElement value is provided, scrollToEdge/scrollBy values will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**scroll_to_element:** `typing.Optional[str]` — A natural language description of where to scroll (e.g. 'the search box', 'username field'). The interaction will be aborted if the target element cannot be found. If provided, scrollToEdge/scrollBy values will be ignored.
    
</dd>
</dl>

<dl>
<dd>

**scroll_within:** `typing.Optional[str]` — A natural language description of the scrollable area on the web page. This identifies the container or region that should be scrolled. If missing, the entire page will be scrolled. You can also describe a visible reference point inside the container. Note: This is different from scrollToElement, which specifies the target element to scroll to. The target may be located inside the scrollable area defined by scrollWithin.
    
</dd>
</dl>

<dl>
<dd>

**time_threshold_seconds:** `typing.Optional[int]` 

A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

This setting does not extend the maximum session duration provided at the time of session creation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">summarize_content</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

This endpoint is deprecated. Please use the `pageQuery` endpoint and ask for a summary in the prompt instead.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.summarize_content(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The session id for the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — The Airtop window id of the browser window to summarize.
    
</dd>
</dl>

<dl>
<dd>

**client_request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[SummaryConfig]` — Request configuration
    
</dd>
</dl>

<dl>
<dd>

**cost_threshold_credits:** `typing.Optional[int]` — A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).
    
</dd>
</dl>

<dl>
<dd>

**prompt:** `typing.Optional[str]` — An optional prompt providing the Airtop AI model with additional direction or constraints about the summary (such as desired length).
    
</dd>
</dl>

<dl>
<dd>

**time_threshold_seconds:** `typing.Optional[int]` 

A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

This setting does not extend the maximum session duration provided at the time of session creation.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.windows.<a href="src/airtop/windows/client.py">type</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Execute a type interaction in a specific browser window
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.windows.type(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    window_id="0334da2a-91b0-42c5-6156-76a5eba87430",
    text="Example text",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — The session id for the window.
    
</dd>
</dl>

<dl>
<dd>

**window_id:** `str` — The Airtop window id of the browser window.
    
</dd>
</dl>

<dl>
<dd>

**text:** `str` — The text to type into the browser window.
    
</dd>
</dl>

<dl>
<dd>

**clear_input_field:** `typing.Optional[bool]` — If true, and an HTML input field is active, clears the input field before typing the text.
    
</dd>
</dl>

<dl>
<dd>

**client_request_id:** `typing.Optional[str]` 
    
</dd>
</dl>

<dl>
<dd>

**configuration:** `typing.Optional[MicroInteractionConfigWithExperimental]` — Request configuration
    
</dd>
</dl>

<dl>
<dd>

**cost_threshold_credits:** `typing.Optional[int]` — A credit threshold that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).
    
</dd>
</dl>

<dl>
<dd>

**element_description:** `typing.Optional[str]` — A natural language description of where to type (e.g. 'the search box', 'username field'). The interaction will be aborted if the target element cannot be found.
    
</dd>
</dl>

<dl>
<dd>

**press_enter_key:** `typing.Optional[bool]` — If true, simulates pressing the Enter key after typing the text.
    
</dd>
</dl>

<dl>
<dd>

**press_tab_key:** `typing.Optional[bool]` — If true, simulates pressing the Tab key after typing the text. Note that the tab key will be pressed after the Enter key if both options are configured.
    
</dd>
</dl>

<dl>
<dd>

**time_threshold_seconds:** `typing.Optional[int]` 

A time threshold in seconds that, once exceeded, will cause the operation to be cancelled. Note that this is *not* a hard limit, but a threshold that is checked periodically during the course of fulfilling the request. A default threshold is used if not specified, but you can use this option to increase or decrease as needed. Set to 0 to disable this feature entirely (not recommended).

This setting does not extend the maximum session duration provided at the time of session creation.
    
</dd>
</dl>

<dl>
<dd>

**wait_for_navigation:** `typing.Optional[bool]` — If true, Airtop AI will wait for the navigation to complete after clicking the element.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Automations
<details><summary><code>client.automations.<a href="src/airtop/automations/client.py">list</a>()</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

List all automations for a given organization
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.automations.list()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/airtop/automations/client.py">update</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Update the description of a specific automation
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.automations.update(
    description="description",
    id="id",
    org_id="orgId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**description:** `str` — New description for the automation
    
</dd>
</dl>

<dl>
<dd>

**id:** `str` — ID of the automation to update
    
</dd>
</dl>

<dl>
<dd>

**org_id:** `str` — Organization ID
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/airtop/automations/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a specific automation by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.automations.get(
    automation_id="automationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**automation_id:** `str` — ID of the automation to retrieve
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.automations.<a href="src/airtop/automations/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete a specific automation
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.automations.delete(
    automation_id="automationId",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**automation_id:** `str` — ID of the automation to delete
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Files
<details><summary><code>client.files.<a href="src/airtop/files/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a list of files filtered by session ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.files.list(
    offset=1,
    limit=10,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of IDs of the sessionId of the files to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit for pagination.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/airtop/files/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.files.create(
    file_name="fileName",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**file_name:** `str` — Name of the file
    
</dd>
</dl>

<dl>
<dd>

**file_type:** `typing.Optional[CreateFileRestInputV1FileType]` — Type of the file
    
</dd>
</dl>

<dl>
<dd>

**id:** `typing.Optional[str]` — File ID. Must be unique. Leave blank to get one generated for you
    
</dd>
</dl>

<dl>
<dd>

**session_ids:** `typing.Optional[typing.Sequence[str]]` — IDs of the associated sessions
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/airtop/files/client.py">get</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.files.get(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the file
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.files.<a href="src/airtop/files/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.files.delete(
    id="id",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the file
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Profiles
<details><summary><code>client.profiles.<a href="src/airtop/profiles/client.py">delete</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Delete profiles matching by id
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.profiles.delete()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**profile_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — DEPRECATED. Use profileNames.
    
</dd>
</dl>

<dl>
<dd>

**profile_names:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of profile names.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Requests
<details><summary><code>client.requests.<a href="src/airtop/requests/client.py">get_request_status</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.requests.get_request_status(
    request_id="123e4567-e89b-12d3-a456-426614174000",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**request_id:** `str` — The ID of the request to check.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

## Sessions
<details><summary><code>client.sessions.<a href="src/airtop/sessions/client.py">list</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a paginated list of sessions filtered by ID or status
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.sessions.list(
    offset=1,
    limit=10,
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_ids:** `typing.Optional[typing.Union[str, typing.Sequence[str]]]` — A comma-separated list of IDs of the sessions to retrieve.
    
</dd>
</dl>

<dl>
<dd>

**status:** `typing.Optional[SessionsListRequestStatus]` — Status of the session to get.
    
</dd>
</dl>

<dl>
<dd>

**offset:** `typing.Optional[int]` — Offset for pagination.
    
</dd>
</dl>

<dl>
<dd>

**limit:** `typing.Optional[int]` — Limit for pagination.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sessions.<a href="src/airtop/sessions/client.py">create</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.sessions.create()

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**configuration:** `typing.Optional[SessionConfigV1]` — Session configuration
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sessions.<a href="src/airtop/sessions/client.py">get_info</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a session by ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.sessions.get_info(
    id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — Id of the session to get
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sessions.<a href="src/airtop/sessions/client.py">terminate</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Ends a session by ID. If a given session id does not exist within the organization, it is ignored.
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.sessions.terminate(
    id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the session to delete.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sessions.<a href="src/airtop/sessions/client.py">events</a>(...)</code></summary>
<dl>
<dd>

#### 📝 Description

<dl>
<dd>

<dl>
<dd>

Get a session event stream for a given session ID
</dd>
</dl>
</dd>
</dl>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
response = client.sessions.events(
    id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    last_event_id=0,
    all_=True,
)
for chunk in response:
    yield chunk

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**id:** `str` — ID of the session to get status info for
    
</dd>
</dl>

<dl>
<dd>

**last_event_id:** `typing.Optional[int]` — last known event id
    
</dd>
</dl>

<dl>
<dd>

**all_:** `typing.Optional[bool]` — Get all events
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

<details><summary><code>client.sessions.<a href="src/airtop/sessions/client.py">save_profile_on_termination</a>(...)</code></summary>
<dl>
<dd>

#### 🔌 Usage

<dl>
<dd>

<dl>
<dd>

```python
from airtop import Airtop

client = Airtop(
    api_key="YOUR_API_KEY",
)
client.sessions.save_profile_on_termination(
    session_id="6aac6f73-bd89-4a76-ab32-5a6c422e8b0b",
    profile_name="myProfile",
)

```
</dd>
</dl>
</dd>
</dl>

#### ⚙️ Parameters

<dl>
<dd>

<dl>
<dd>

**session_id:** `str` — ID of the session.
    
</dd>
</dl>

<dl>
<dd>

**profile_name:** `str` — Name under which to save the profile.
    
</dd>
</dl>

<dl>
<dd>

**request_options:** `typing.Optional[RequestOptions]` — Request-specific configuration.
    
</dd>
</dl>
</dd>
</dl>


</dd>
</dl>
</details>

