import webbrowser

import gradio as gr
import os

with gr.Blocks() as demo:
    gr.Markdown("# Greetings from Gradio!")
    inp = gr.Textbox(placeholder="What is your name?")
    out = gr.Textbox()

    inp.change(fn=lambda x: f"Welcome, {x}!",
               inputs=inp,
               outputs=out)
    folder_path = r"C:\RnD\jlukhi\python_projects\tesing_data\files2_tmp"

    file_list = [os.path.join(folder_path, file_name) for file_name in os.listdir(folder_path)]
    chosen_collection = gr.Dropdown(
        file_list, label="Index Collection name", info="Choose collection for get ans"
    )

    get_indexed_dbs_btn = gr.Button(value="Get indexed dbs", scale=0, size='sm',
                                    visible=True)


    def get_indexed_list(x=None):
        indexed_collection_dir = 'db_collections'
        if not os.path.exists(indexed_collection_dir):
            os.makedirs(indexed_collection_dir)
        print(os.listdir(indexed_collection_dir))
        return [[file_name for file_name in os.listdir(indexed_collection_dir)]]
        # return [os.path.join(indexed_collection_dir, file_name) for file_name in os.listdir(indexed_collection_dir)]


    def update_dropdown(x):
        return gr.Dropdown.update(choices=x, value=[1, 2])


    indexed_collections_list = []
    collections_list = gr.Dropdown(
        indexed_collections_list,
        value=[],
        label="Collections List",
        interactive=True,
        visible=True)

    # eventdb4 = get_indexed_dbs_btn.click(fn=update_dropdown, inputs=get_indexed_list,
    #                                      outputs=collections_list)

    get_sources_args = dict(fn=get_indexed_list,
                            inputs=None,
                            outputs=indexed_collections_list,
                            # queue=queue,
                            # api_name='get_indexed_sources' if allow_api else None
                            )

    eventdb4 = get_indexed_dbs_btn.click(**get_sources_args) \
        .then(fn=update_dropdown, inputs=indexed_collections_list, outputs=collections_list)

if __name__ == "__main__":
    demo.launch(server_name="localhost", show_error=True, server_port=8082)
    # webbrowser.open(demo.local_url)
