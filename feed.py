import yaml
import xml.etree.ElementTree as xml_tree

# Change this to your GitHub Pages or website URL
link_prefix = "https://Sonu1747.github.io/podcast"

# Read YAML
with open("feed.yaml", "r", encoding="utf-8") as file:
    yaml_data = yaml.safe_load(file)

# Root RSS element
rss_element = xml_tree.Element(
    "rss",
    {
        "version": "2.0",
        "xmlns:itunes": "http://www.itunes.com/dtds/podcast-1.0.dtd",
        "xmlns:content": "http://purl.org/rss/1.0/modules/content/",
    },
)

# Channel
channel_element = xml_tree.SubElement(rss_element, "channel")

xml_tree.SubElement(channel_element, "title").text = yaml_data["title"]
xml_tree.SubElement(channel_element, "itunes:subtitle").text = yaml_data["subtitle"]
xml_tree.SubElement(channel_element, "itunes:author").text = yaml_data["author"]
xml_tree.SubElement(channel_element, "description").text = yaml_data["description"]
xml_tree.SubElement(
    channel_element,
    "itunes:image",
    {"href": link_prefix + yaml_data["image"]},
)
xml_tree.SubElement(channel_element, "language").text = yaml_data["language"]
xml_tree.SubElement(channel_element, "link").text = link_prefix
xml_tree.SubElement(
    channel_element,
    "itunes:category",
    {"text": yaml_data["category"]},
)

xml_tree.SubElement(channel_element, "lastBuildDate").text = yaml_data["item"][-1]["published"]

# Episodes
for item in yaml_data["item"]:
    item_element = xml_tree.SubElement(channel_element, "item")

    xml_tree.SubElement(item_element, "title").text = item["title"]
    xml_tree.SubElement(item_element, "itunes:author").text = yaml_data["author"]
    xml_tree.SubElement(item_element, "description").text = item["description"]
    xml_tree.SubElement(item_element, "itunes:duration").text = item["duration"]
    xml_tree.SubElement(item_element, "pubDate").text = item["published"]

    xml_tree.SubElement(
        item_element,
        "enclosure",
        {
            "url": link_prefix + item["file"],
            "type": yaml_data["format"],
            "length": str(item["length"]),
        },
    )

# Save XML
output_tree = xml_tree.ElementTree(rss_element)
output_tree.write(
    "podcast.xml",
    encoding="UTF-8",
    xml_declaration=True,
)

print("✅ podcast.xml generated successfully!")