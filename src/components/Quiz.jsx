
import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

function Quiz() {
  const navigate = useNavigate();

  const userQuestions = [
    'هل نشأت في بيئة أسرية مستقرة؟',
    'هل كان أحد والديك غائبًا لفترات طويلة؟',
    'هل تعرضت لتجارب عاطفية مؤثرة في سن مبكرة؟',
    'هل كنت تشعر بالأمان في طفولتك؟',
    'هل كنت تتجنب التعبير عن مشاعرك في المنزل؟',
    'هل كان والداك يعبران عن مشاعرهما بوضوح؟',
    'هل كنت تتحمل مسؤوليات مبكرة في طفولتك؟',
    'هل تعتقد أن والدتك كانت حنونة ومتفاعلة معك؟',
  ];

  const partnerQuestions = [
    'هل تعتقد أن شريكك نشأ في بيئة مستقرة؟',
    'هل تشعر أن شريكك يعاني من غياب عاطفي سابق؟',
    'هل شريكك يعبّر عن مشاعره بسهولة؟',
    'هل تظن أن شريكك يفضّل تجنّب المواجهة؟',
    'هل لدى شريكك تجربة عاطفية مؤلمة؟',
    'هل لاحظت ميل شريكك لتحمّل مسؤولية مفرطة؟',
    'هل شريكك يتحدث عن والدته بشكل إيجابي؟',
    'هل يفضل شريكك الصمت عند التوتر؟',
  ];

  const expectationQuestions = [
    'ما مدى أهمية التواصل العاطفي في العلاقة؟',
    'هل تعتبر الاستقرار المالي شرطًا أساسيًا؟',
    'هل تعتقد أن الحب وحده يكفي لاستمرار العلاقة؟',
    'هل تفضل علاقة تتضمن مشاركة يومية مكثفة؟',
    'هل ترى أن الغيرة دليل حب؟',
    'هل تخطط للزواج خلال السنة القادمة؟',
    'هل تشعر أنك جاهز نفسيًا للالتزام؟',
    'هل تسامح الخيانة بسهولة؟',
    'هل تحب أن تُفاجأ عاطفيًا؟',
    'هل تخشى من تكرار تجاربك السابقة؟',
  ];

  const totalQuestions = [
    ...userQuestions.map((q, i) => ({ text: q, category: 'user', id: `u${i}` })),
    ...partnerQuestions.map((q, i) => ({ text: q, category: 'partner', id: `p${i}` })),
    ...expectationQuestions.map((q, i) => ({ text: q, category: 'expectation', id: `e${i}` })),
  ];

  const [currentIndex, setCurrentIndex] = useState(0);
  const [answers, setAnswers] = useState({});

  const handleAnswer = (value) => {
    const currentQuestion = totalQuestions[currentIndex];
    const updatedAnswers = {
      ...answers,
      [currentQuestion.id]: {
        category: currentQuestion.category,
        answer: value
      }
    };
    setAnswers(updatedAnswers);

    if (currentIndex + 1 < totalQuestions.length) {
      setCurrentIndex(currentIndex + 1);
    } else {
      localStorage.setItem('quizAnswers', JSON.stringify(updatedAnswers));
      navigate('/analyzer');
    }
  };

  const current = totalQuestions[currentIndex];

  return (
    <div className="quiz-container">
      <h2>الاستبيان المبدئي</h2>
      <p>
        {current.category === 'user' && '🧒 عن طفولتك'}
        {current.category === 'partner' && '💬 عن شريكك'}
        {current.category === 'expectation' && '🎯 عن توقعاتك'}
      </p>
      <h3>{current.text}</h3>
      <div className="button-group">
        <button onClick={() => handleAnswer('نعم')}>نعم</button>
        <button onClick={() => handleAnswer('لا')}>لا</button>
        <button onClick={() => handleAnswer('أحيانًا')}>أحيانًا</button>
      </div>
      <p>
        {currentIndex + 1} / {totalQuestions.length}
      </p>
    </div>
  );
}

export default Quiz;
