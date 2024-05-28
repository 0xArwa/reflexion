from langchain.prompts import PromptTemplate


COT_SIMPLE_INSTRUCTION = """نفذ التعليمات بدقة بناءً على تفكير منطقي للسياق. تأكد من أن ردك مُتناسق ومنطقي، مع استخدام خيار "إنهاء [الإجابة]" لإنهاء المهمة وإرسال ردك النهائي.
يمكنك مراجعة بعض الأمثلة التالية:
{examples}
(نهاية الامثلة)
{reflections}
{context}
التعليمات: {question}{scratchpad}"""


COT_INSTRUCTION = """نفذ التعليمات بدقة بناءً على تفكير منطقي للسياق. تأكد من أن ردك مُتناسق ومنطقي، مع استخدام خيار "إنهاء [الإجابة]" لإنهاء المهمة وإرسال ردك النهائي. سيتم تزويدك بالسياق الذي يجب أن تستخدمه لمساعدتك في تنفيذ المطلوب.
يمكنك مراجعة بعض الأمثلة التالية:
{examples}
(نهاية الامثلة)
{reflections}
السياق: {context} 
التعليمات: {question}{scratchpad}"""


COT_REFLECT_INSTRUCTION = """بصفتك وكيلًا يتمتع بمهارات استدلال منطقي قابلة للتحسين من خلال تقييم الذات، ستتلقى سياقًا من الماضي يتضمن التعليمات والرد الذي قدمته سابقًا. نظرًا لعدم قدرتك على الإجابة على السؤال بشكل صحيح، فهناك سببان محتملان: إما أنك خمنت إجابة خاطئة باستخدام خيار "إنهاء[الإجابة]"، أو أن هناك اختلافًا في صياغة إجابتك مقارنة بالإجابة الصحيحة. في غضون جملتين أو ثلاث، حدد سببًا محتملاً للفشل أو التناقض في ردك السابق، ثم اقترح خطة جديدة دقيقة وموجزة تهدف إلى تجنب تكرار هذه الأخطاء. استخدم جملًا كاملة في صياغة ردك.
يمكنك مراجعة بعض الأمثلة التالية:
{examples}
(نهاية الامثلة)

المحاولة السابقة:
السياق: {context}
التعليمات: {question}{scratchpad}

النقد البناء:"""

COT_AGENT_REFLECT_INSTRUCTION = """اقرأ التعليمات بعناية وافهمها جيدًا قبل الرد. تأكد من ربط أفكارك بالمعلومات المُقدمة واتّخذ قرارات تتوافق مع السياق. أخيرًا، قدم ردك الكامل باستخدام "إنهاء[الرد]".
يمكنك مراجعة بعض الأمثلة التالية:
{examples}
(نهاية الامثلة)

{reflections}

السياق: {context}
التعليمات: {question}{scratchpad}"""


COT_SIMPLE_REFLECT_INSTRUCTION = """بصفتك وكيلًا يتمتع بمهارات استدلال منطقي قابلة للتحسين من خلال تقييم الذات، ستتلقى سياقًا من الماضي يتضمن التعليمات والرد الذي قدمته سابقًا. نظرًا لعدم قدرتك على الإجابة على السؤال بشكل صحيح، فهناك سببان محتملان: إما أنك خمنت إجابة خاطئة باستخدام خيار "إنهاء[الإجابة]"، أو أن هناك اختلافًا في صياغة إجابتك مقارنة بالإجابة الصحيحة. في غضون جملتين أو ثلاث، حدد سببًا محتملاً للفشل أو التناقض في ردك السابق، ثم اقترح خطة جديدة دقيقة وموجزة تهدف إلى تجنب تكرار هذه الأخطاء. استخدم جملًا كاملة في صياغة ردك.
يمكنك مراجعة بعض الأمثلة التالية:
{examples}
(نهاية الامثلة)
{context}
المحاولة السابقة:
التعليمات: {question}{scratchpad}

النقد البناء:"""

COT_SIMPLE_AGENT_REFLECT_INSTRUCTION = """نفذ التعليمات بدقة بناءً على تفكير منطقي للسياق. تأكد من أن ردك مُتناسق ومنطقي، مع استخدام خيار "إنهاء [الإجابة]" لإنهاء المهمة وإرسال ردك النهائي.
يمكنك مراجعة بعض الأمثلة التالية:
{examples}
(نهاية الامثلة)
{reflections}
{context}
التعليمات: {question}{scratchpad}"""

REFLECTION_HEADER = 'سبق وأن جربت الإجابة على هذا السؤال، لكن دون نجاح. تقدم لك التقييمات التالية خطة لتجنب تكرار نفس الخطأ. استفد منها لتحسين استراتيجيتك وتقديم إجابة صحيحة على السؤال المطروح.  \n'
REFLECTION_AFTER_LAST_TRIAL_HEADER = 'تقدم لك التقييمات التالية خطة لتجنب تكرار نفس الخطأ عند الإجابة على هذا السؤال. استفد منها لتحسين استراتيجيتك وتقديم إجابة صحيحة على السؤال المطروح. \n'
LAST_TRIAL_HEADER = 'لقد حاولت الإجابة على السؤال التالي مسبقا ولكن لم تنجح. تجد أدناه آخر محاولة قمت بها للإجابة على السؤال.'


cot_simple_agent_prompt = PromptTemplate(
                        input_variables=["examples", "question", "reflections", "context", "scratchpad"],
                        template = COT_SIMPLE_INSTRUCTION,
                        )

cot_reflect_agent_prompt = PromptTemplate(
                        input_variables=["examples", "reflections", "context", "question", "scratchpad"],
                        template = COT_AGENT_REFLECT_INSTRUCTION,
                        )

cot_agent_prompt = PromptTemplate(
                        input_variables=["examples", "reflections", "context", "question", "scratchpad"],
                        template = COT_INSTRUCTION,
                        )

cot_simple_reflect_prompt = PromptTemplate(
                        input_variables=["examples", "question", "context", "scratchpad"],
                        template = COT_SIMPLE_REFLECT_INSTRUCTION,
                        )

cot_simple_reflect_agent_prompt = PromptTemplate(
                        input_variables=["examples", "context", "reflections", "question", "scratchpad"],
                        template = COT_SIMPLE_AGENT_REFLECT_INSTRUCTION,
                        )

cot_reflect_prompt = PromptTemplate(
                        input_variables=["examples", "context", "question", "scratchpad"],
                        template = COT_REFLECT_INSTRUCTION,
                        )




