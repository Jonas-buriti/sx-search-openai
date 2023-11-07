import { Example } from "./Example";

import styles from "./Example.module.css";

export type ExampleModel = {
    text: string;
    value: string;
};

const EXAMPLES: ExampleModel[] = [
    {
        text: `Quais são os direitos de uso da novela "A Infância de Romeu e Julieta"`,
        value: `Quais são os direitos de uso da novela "A Infância de Romeu e Julieta"`
    },
    { text: "O que pode me dizer sobre a M&M EVENTOS LTDA?", value: "O que pode me dizer sobre a M&M EVENTOS LTDA?" },
    { text: "Qual o pacote de mídia/entregas da Mattel?", value: "Qual o pacote de mídia/entregas da Mattel?" }
];

interface Props {
    onExampleClicked: (value: string) => void;
}

export const ExampleList = ({ onExampleClicked }: Props) => {
    return (
        <ul className={styles.examplesNavList}>
            {EXAMPLES.map((x, i) => (
                <li key={i}>
                    <Example text={x.text} value={x.value} onClick={onExampleClicked} />
                </li>
            ))}
        </ul>
    );
};
