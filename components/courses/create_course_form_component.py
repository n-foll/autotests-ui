from playwright.sync_api import Page
import allure
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

    @allure.step('Check visible empty view title "{title}", and  estimated time "{estimated_time}", and description "{description}", and max score "{max_score}", and min score "{min_score}"')
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

    @allure.step('Fill create course')
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