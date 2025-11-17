from playwright.sync_api import Page
from components.base_component import BaseComponent
from elements.input import Input
from elements.textarea import Textarea

class CreateCourseFormComponent(BaseComponent):
    def __init__(self, page: Page):
        super().__init__(page)

        self.course_title = Input(page,'create-course-form-title-input', 'Email')
        self.course_estimated_time = (
           Input(page,'create-course-form-estimated-time-input', 'Estimated Time')
        )
        self.create_course_description_textarea = (
            Textarea(page, 'create-course-form-description-input', 'Desription')
        )
        self.create_course_max_score_input = Input(page, 'create-course-form-max-score-input', 'Max Score')
        self.create_course_min_score_input = Input(page, 'create-course-form-min-score-input', 'Min Score')

    def check_visible_create_course(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.course_title.check_visible()
        self.course_title.check_have_value(title)

        self.course_estimated_time.check_visible()
        self.course_estimated_time.check_have_value(estimated_time)

        self.create_course_description_textarea.check_visible()
        self.create_course_description_textarea.check_have_value(description)

        self.create_course_max_score_input.check_visible()
        self.create_course_max_score_input.check_have_value(max_score)

        self.create_course_min_score_input.check_visible()
        self.create_course_min_score_input.check_have_value(min_score)

    def fill_create_course(
            self,
            title: str,
            estimated_time: str,
            description: str,
            max_score: str,
            min_score: str
    ):
        self.course_title.fill(title)
        self.course_title.check_have_value(title)

        self.course_estimated_time.fill(estimated_time)
        self.course_estimated_time.check_have_value(estimated_time)

        self.create_course_description_textarea.fill(description)
        self.create_course_description_textarea.check_have_value(description)

        self.create_course_max_score_input.fill(max_score)
        self.create_course_max_score_input.check_have_value(max_score)

        self.create_course_min_score_input.fill(min_score)
        self.create_course_min_score_input.check_have_value(min_score)