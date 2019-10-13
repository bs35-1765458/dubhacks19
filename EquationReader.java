package com.example.equationsreader;

        import androidx.appcompat.app.AppCompatActivity;
        import androidx.core.app.ActivityCompat;

        import android.Manifest;
        import android.content.pm.PackageManager;
        import android.os.Bundle;
        import android.speech.tts.TextToSpeech;
        import android.view.View;
        import android.widget.TextView;

        import com.itextpdf.text.pdf.PdfReader;
        import com.itextpdf.text.pdf.parser.PdfTextExtractor;

        import java.io.File;
        import java.io.IOException;
        import java.util.Locale;

public class EquationReader extends AppCompatActivity {

    private TextView textView;
    private TextToSpeech textToSpeech;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_equation_reader);

        textView = findViewById(R.id.textView);

        textToSpeech = new TextToSpeech(getApplicationContext(), new TextToSpeech.OnInitListener() {
            @Override
            public void onInit(int i) {
                textToSpeech.setLanguage(Locale.US);
            }
        });

        ActivityCompat.requestPermissions(this, new String[]{Manifest.permission.READ_EXTERNAL_STORAGE, Manifest.permission.WRITE_EXTERNAL_STORAGE}, PackageManager.PERMISSION_GRANTED);
    }

    public void readButtonOnClick(View view){
        File file = new File("/sdcard/myPDFFile.pdf");

        String stringParser;

        try {
            PdfReader pdfReader = new PdfReader(file.getPath());
            stringParser = PdfTextExtractor.getTextFromPage(pdfReader, 1).trim();
            pdfReader.close();
            textView.setText(stringParser);
            textToSpeech.speak(stringParser, TextToSpeech.QUEUE_FLUSH,null, null);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
