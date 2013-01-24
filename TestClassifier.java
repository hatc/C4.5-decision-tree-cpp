// test C4.5 decision tree
// Copyright (C) 2012-2013 Yuri Agafonov
// All rights reserved.
// 
// Redistribution and use in source and binary forms, with or without
// modification, are permitted provided that the following conditions are met:
// 
// 1. Redistributions of source code must retain the above copyright notice, this
// list of conditions and the following disclaimer.
// 2. Redistributions in binary form must reproduce the above copyright notice,
// this list of conditions and the following disclaimer in the documentation
// and/or other materials provided with the distribution.
//
// THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND
// ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
// WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
// DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR
// ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES
// (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES;
// LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND
// ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT
// (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
// SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

import java.io.*;

import weka.core.Attribute;
/*import weka.core.Capabilities;
import weka.core.Capabilities.Capability;*/
import weka.core.Instance;
import weka.core.Instances;
/*import weka.core.RevisionUtils;
import weka.classifiers.Classifier;*/

class TestClassifier {
	static Instances loadData(String file_path, Integer class_index) {
		Instances r = null;
		BufferedReader reader = null;
		try {
			reader = new BufferedReader(new FileReader(file_path));
			r = new Instances(reader);
			if (class_index != null)
				r.setClassIndex(class_index.intValue());
			else
				r.setClassIndex(r.numAttributes() - 1);
		} catch (FileNotFoundException e) {
			System.out.println("can't find file: '" + file_path + "'");
		} catch (IOException e) {
			e.printStackTrace(System.out);
		} finally {
			try {
				if (reader != null)
					reader.close();
			} catch (IOException e) {}
		}
		return r;
	}
	
	static double classifyInstance(Instance i) throws Exception {
    Object[] s = new Object[i.numAttributes()];
    
    for (int j = 0; j < s.length; j++) {
      if (!i.isMissing(j)) {
        if (i.attribute(j).isNominal())
          s[j] = new String(i.stringValue(j));
        else if (i.attribute(j).isNumeric())
          s[j] = new Double(i.value(j));
      }
    }
    
    // set class value to missing
    s[i.classIndex()] = null;
    
    return WekaJ48Classifier.classify(s);
    //return J48Classificator.classify(s);
  }
  
  /*Capabilities getCapabilities() {
  	weka.core.Capabilities result = new weka.core.Capabilities(this);
  	
  	result.enable(weka.core.Capabilities.Capability.NOMINAL_ATTRIBUTES);
    result.enable(weka.core.Capabilities.Capability.NUMERIC_ATTRIBUTES);
    result.enable(weka.core.Capabilities.Capability.DATE_ATTRIBUTES);
    result.enable(weka.core.Capabilities.Capability.MISSING_VALUES);
    result.enable(weka.core.Capabilities.Capability.NOMINAL_CLASS);
    result.enable(weka.core.Capabilities.Capability.MISSING_CLASS_VALUES);

    result.setMinimumNumberInstances(0);

    return result;
  }*/
	
	public static void main(String args[]) throws Exception {
		if (args.length > 1) {
			System.out.println("path to the ARFF data set file required");
			return;
		}
		
		Integer class_index = null;
		if (args.length > 2) {
			try {
				class_index = Integer.valueOf(args[1], 10);
			} catch (NumberFormatException e) {}
		}
		
		Instances data = loadData(args[0], class_index);
		// can classifier handle the data?
		// getCapabilities().testWithFail(data);
		
		// for (Instance i : IterableEnumeration.make(Instance.class, loadData(args[0], class_index).enumerateInstances())) {
		for (Instance i : IterableEnumeration.make(Instance.class, data.enumerateInstances())) {
			double r = classifyInstance(i);
			if (r != r) {
				System.out.println("NaN");
			} else {
				System.out.println((int)r);
			}
		}
	}
}
