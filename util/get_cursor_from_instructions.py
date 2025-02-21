def get_cursor_from_instructions(instructions: list) -> str:
    cursor = None
    for instruction in instructions:
        if instruction["type"] == "TimelineAddEntries":
            entries = instruction["entries"]
            for entry in entries:
                if entry["content"]["entryType"] == "TimelineTimelineCursor":
                    cursor = entry["content"]["value"]
                    break
                if entry["content"]["entryType"] == "TimelineTimelineItem":
                    if entry["content"]["itemContent"]["itemType"] == "TimelineTimelineCursor":
                        cursor = entry["content"]["itemContent"]["value"]
                        break
    return cursor