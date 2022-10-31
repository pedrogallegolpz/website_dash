import dash
from dash import html, dcc 
import dash_bootstrap_components as dbc
from .side_bar import sidebar

dash.register_page(__name__, path="/project_tfg", name='Grad-CAM Computer Vision')

def layout():
    return html.Div(
        [
            dbc.Row(
                [
                    dbc.Col(
                        [sidebar()],
                        xs=4, sm=4, md=2, lg=2, xl=2, xxl=2, # set the dimension of the col in function of windows size
                        # xs=extra small, sm=small, md=middle, lg=large, xl=extra-large, xxl=extra-extra large
                    )
                    ,

                    dbc.Col(
                        [
                            html.Br(),
                            html.H3('Grad-CAM Computer Vision', style={'color': 'rgba(255,255,255)'}),
                            dcc.Markdown(" [GitHub](https://github.com/pedrogallegolpz/TFG)"),
                            html.Br(),

                            dcc.Markdown(
                                """
                                This project was born with my final dual bachelor thesis where I studied the ability of Class Activation Maps methods for segmentation and detectetion problems. I studied the performance of unsupervised methods for segmentation. These methods are the Grad-CAM family: CAM, Grad-CAM, Grad-CAM++ and Smooth Grad-CAM++.
                                """, style={'textAlign':'justify','whiteSpace': 'pre-wrap'}),


                            html.Br(),
                            html.Div(
                                html.Img(src='assets/tfg.png', width='100%')
                                , style={'background-color':"rgba(255,255,255,0.1)"}),
                            html.Br(),
                            html.Br(),

                            dcc.Markdown("#### Abstract", style={'color':'white'}),
                            dcc.Markdown(
                                """
                                The boom of Artificial Intelligence in the world came a few years ago, when professions
                                in all disciplines began to see its potential and tried to find applications in
                                their sector. This explosion arrived with the mathematical models of Machine Learning.
                                It was in fact the concept of machine learning that caused a revolution within
                                humans themselves, breaking a fictional barrier created by humans many years ago.
                                It was seen how Deep Learning models were able to solve very complex tasks with
                                high performance. An example could be a Convolutional Network model solving a
                                medical imaging diagnosis problem, where a human who is not skilled in the field
                                would be unable to solve it. Such powerful results increased the confidence placed in
                                this technology. Now, following the example, doctors could use this tool to diagnose,
                                saving them effort and time.
                            
                                """, style={'textAlign':'justify'}),
                            dcc.Markdown(
                                """
                                However, Artificial Intelligence would have a barrier: explainability. Determining
                                what decision to make when the doctor had a different opinion on the diagnosis than
                                the deep learning model’s opinion became a problem. The complexity of the models
                                made it impossible to understand why they made those decisions, deeming them
                                black boxes, completely opaque. This caused the doctor to make decisions solely on
                                his own judgement, because if both the doctor and the model gave the same diagnosis
                                then his judgement was followed; but if the doctor gave a diagnosis different from
                                that of the model, the doctor was likely to follow his diagnosis because he understood
                                it, assuming that the model could have been wrong in that case.
                                At this point XAI (eXplicable Artificial Intelligence) appeared whose mission was
                                to provide Artificial Intelligence tools ensuring transparency in these models. This
                                new field of study opened a wide variety of doors, such as ethics within Artificial
                                Intelligence, where ethics can now be assessed within the decision field of the model;
                                explainability for experts in the area of application of the model (such as doctors),
                                allowing them to understand the results in order to help their own criteria; or explainability
                                for experts in Artificial Intelligence (data scientists for example), detecting
                                flaws in the model such as biases or other types of errors that may affect the goodness
                                of the results.
                            
                                """, style={'textAlign':'justify'}),
                            dcc.Markdown(
                                """
                                Class Activation Map methods are tools that emerged from XAI in the area of Computer
                                Vision. These methods or techniques allow you to understand what the model
                                has been based on to give the results it has produced. They visually create an activation
                                map of the input, highlighting those regions that have been particularly relevant
                                to the decision-making process. In the problem of diagnostic medical imaging, these
                                techniques were able to determine which parts of the image were most relevant to the
                                diagnosis. This meant that if the diagnosis was positive (pathological features), the
                                techniques were able to determine the region where those features that marked the
                                presence of pathology were found. So, these techniques were very powerful because
                                it had achieved those models trained for classification were able to solve the task of
                                unsupervised localization. Now, in this type of image-based diagnosis, a doctor can
                                use these models judiciously, using them as a complement to his knowledge.
                                The object of study of this work is precisely the application of Class Activation
                                Map (CAM) methods to the medical imaging diagnosis discussed in the example. After
                                the first published paper on Class Activation Map, advances and improvements
                                were made: Gradient-wieghted Class Activation Mapping (Grad-CAM) which relaxed
                                the constraints of the network architecture with the help of the gradient of the
                                output with respect to the activations, Grad-CAM++ which achieves improvements
                                in multiple locations of the same class and Smooth Grad-CAM++ which incorporates
                                more images identical to the original with added noise to improve the decision making
                                and smooth the activation map. These techniques have been implemented and
                                can be accessed via [github.com/pedrogallegolpz/TFG](https://github.com/pedrogallegolpz/TFG).
                            
                                """, style={'textAlign':'justify'}),
                            dcc.Markdown(
                                """
                                We have, therefore, four explainability techniques: each one is supposed to be more
                                powerful than its predecessor. In this study we are going to study which technique
                                behaves better and is more manageable in this problem, making an depth analysis of
                                how they behave. These techniques are applied on existing models, so in order not
                                to bias the results, they will be studied by taking four different base convolutional
                                networks: VGG16, RESNET18, MOBILENETv2 and EFFICIENTNETb0. This results in
                                four results for each technique and four results for each model. Although the CAM
                                method is shown in the study, it will not be evaluated in the comparison between
                                techniques since it has an architecture restriction (it can only have at most one fully
                                connected layer in its classifier), Grad-CAM being a direct generalisation of CAM for
                                models with architectures that can have more than one fully connected layer in the
                                classifier.
                            
                                """, style={'textAlign':'justify'}),
                            dcc.Markdown(
                                """
                                The study is performed on a publicly accessible prostate histological image dataset:
                                SICAPv1. These are large images of 79 patients. The source of the dataset ensures
                                pixel accuracy for the labelling of the masks. However, it is possible to get examples
                                where the mask picks up areas where there is background as tissue. The images have
                                had to be processed to decrease their size and consequently cause an increase in the
                                number of instances of the dataset to be used. This image processing causes problems
                                in the study of explainability, creating bias in the dataset with images that have a large
                                percentage of pathological tissue in their domain and causing inconsistencies in the
                                location of pathological tissue in contiguous images. These problems coupled with
                                inaccurate labelling of the masks will lead to an error in the localisation metrics of
                                the study.
                            
                                """, style={'textAlign':'justify'}),
                            dcc.Markdown(
                                """
                                Problems such as those discussed with the dataset, coupled with the intrinsic localisation
                                limitations of these techniques, will cause the quality of the results to be
                                strictly limited to less than perfect. The intrinsic limitations of the techniques have to
                                do with the resizing of the activation map or heat map: by resizing to a larger size
                                (the dimensions of the input), pixel precision is lost, making it impossible to adjust
                                to any region where there is pathological tissue.
                            
                                """, style={'textAlign':'justify'}),
                            dcc.Markdown(
                                """
                                The proposal made in the work is to make a separate comparison between models
                                and techniques. The idea is to take the best network among the four by making an
                                overall assessment of the techniques on each model. On the other hand, taking the
                                best technique among the four, a global evaluation of the models will be made on each
                                technique. At the end there will be one best model and one best technique, which will
                                be the winning pair. This implies that the best pair may be the pair that does not have
                                the best mark in any of the metrics on which they are evaluated. In terms of results,
                                one would expect the best model to be the one with the most innovative architecture
                                and the best technique to be the one that has incorporated the most improvements.
                                But no, the classical model based on VGG16 is the best together with the Grad-CAM
                                base technique. In this decision, computational times were important, as there was
                                no clear winner among the techniques.
                            
                                """, style={'textAlign':'justify'}),
                            dcc.Markdown(
                                """
                                It can be seen that factors such as the classification capability of a model directly
                                influence the localisation capability of these techniques. The Smooth Grad-CAM++
                                technique offers a strong dependence on the model and the dataset, which makes it
                                unsuitable both for its computational time and the difficulty of parameterising it well.
                                Finally, the solutions provided by the best combination of model and technique are
                                of sufficient quality to be incorporated into the day-to-day work of a doctor and thus
                                to value the help that this tool offers to the expert. The avenues for future work are
                                multiple and this is just a small approximation of what Artificial Intelligence can do
                                to help in an essential area such as medicine.
                            
                                """, style={'textAlign':'justify'}),
                            dcc.Markdown(
                                """
                                A test code of the tool is available within Google Colab, which can be accessed
                                from the project’s GitHub: [github.com/pedrogallegolpz/TFG](https://github.com/pedrogallegolpz/TFG).
                                """, style={'textAlign':'justify'}),
                            



                            html.Br(),
                            html.Br(),
                            html.Br(),




                        ], 
                        xs=8, sm=8, md=10, lg=10, xl=10, xxl=10
                    )

                ]
            )
        ]
    )

